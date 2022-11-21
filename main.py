
import numpy as np
from presets import PRESETS

def generate_hamiltonian(c):
    """
    Construct Hamiltonian matrix from the given connectivities.
    alpha is set to 0 and beta is set to 1 for ease of computation.
    """
    H = np.zeros((len(c),len(c)))
    for i in range(len(c)):
        for j in c[i]:
            H.itemset((i,j-1),1)
    return H

def get_energies(evalues):
    """
    Sort the list of eigenvalues and round to 12 decimal places to account for
    numerical errors. Return a two dimensional array containing the unique
    energies and the associated degeneracy.
    """
    rounded_values = np.round(evalues,12)
    rounded_values = np.sort(rounded_values)
    e, d = np.unique(rounded_values, return_counts = True)
    energies = [e,d]
    return energies

def print_energies(energies):
    """
    For each orbital energy, print the energy and its degeneracy nicely.
    """
    print("----------------")
    print("Orbital energies: \n")
    for i in range(len(energies[0])):
        e = energies[0][i]
        d = energies[1][i]
        if e >= 0:
            print("Energy:\ta + %.3f b\tDegeneracy: %s" % (e,d))
        else:
            e = -1 * e
            print("Energy:\ta - %.3f b\tDegeneracy: %s" % (e,d))

def welcome_message():
    print("----------------")
    print("General Huckel Solver")

def commands():
    print("----------------")
    print("Available commands:\n")
    print("linear\tfind orbital energies for a linear polyene with n carbons")
    print("cyclic\tfind orbital energies for a cyclic polyene with n carbons")
    print("presets\tdisplay a list of available preset molecules")
    print("custom\tfind orbital energies for a molecule with specified" +
    " connectivity")
    print("help\tdisplay this list of commands")
    print("quit\texits the program")

def connectivity_input():
    valid = False
    while not valid:
        command = input("").lower().strip()
        if command == "linear":
            return linear()
        elif command == "cyclic":
            return cyclic()
        elif command == "presets":
            show_presets()
        elif command in PRESETS.keys():
            return PRESETS[command]
        elif command == "custom":
            return custom()
        elif command == "help":
            commands()
        elif command == "quit":
            exit()
        else:
            print("Invalid command")

def linear():
    """
    Generate connectivity array for a linear molecule of length n
    """
    n = get_n(2)
    connectivities = [[]] * n
    for i in range(n):
        if i == 0:
            connectivities[i] = [2]
        elif i == n-1:
            connectivities[i] = [n-1]
        else:
            connectivities[i] = [i, i+2]
    return connectivities

def cyclic():
    """
    Generate connectivity array for a cyclic molecule of length n
    """
    n = get_n(3)
    connectivities = [[]] * n
    for i in range(n):
        if i == 0:
            connectivities[i] = [2,n]
        elif i == n-1:
            connectivities[i] = [1,n-1]
        else:
            connectivities[i] = [i, i+2]
    return connectivities

def custom():
    """
    Allow for user input molecules
    """
    print("----------------")
    print("Custom molecule input")
    print("To add a bond between two atoms, type \'add\'")
    print("To remove a bond, type \'remove\'")
    print("To view all current bonds, type \'bonds\'")
    print("To finish, type \'done\'")

    bonds = []

    while True:
        inp = input("").lower().strip()
        if inp == "done":
            con = generate_connectivities(bonds)
            #For debugging purposes:
            print(con)
            return con
        elif inp == "bonds":
            show_bonds(bonds)
        elif inp == "add":
            a = get_n(1, "Enter atom 1: ")
            b = get_n(1, "Enter atom 2: ")
            if a == b:
                print("Atom cannot be bonded to itself")
            elif [min(a,b),max(a,b)] in bonds:
                print("Bond already exists")
            else:
                bonds = bonds + [[min(a,b),max(a,b)]]
                print("Bond added")
        elif inp == "remove":
            a = get_n(1, "Enter atom 1: ")
            b = get_n(1, "Enter atom 2: ")
            try:
                bonds.remove([min(a,b),max(a,b)])
            except:
                pass
            print("Bond succesfully removed")

        else:
            print("Invalid input")

    return con

def generate_connectivities(bonds):
    """
    Generate connectivity array from specified bonds
    """
    #Find highest numbered atom
    n = 0
    for b in bonds:
        if b[1] > n:
            n = b[1]

    #Create array to store connectivities
    con = []
    for i in range(n):
        con.append([])

    #Update connectivities according to specified bonds
    for bond in bonds:
        a = bond[0]
        b = bond[1]
        if a not in con[b-1]:
            con[b-1].append(a)
        if b not in con[a-1]:
            con[a-1].append(b)

    return con

def show_bonds(bonds):
    print("Current bonds:")
    for b in bonds:
        print("Atom %s \t- Atom %s" % (b[0], b[1]))

def get_n(min, prompt="Please enter number of carbons: "):
    """
    Handle user input of an integer with a specified minimum value
    """
    valid = False
    while not valid:
        try:
            n = int(input(prompt))
            if n < min:
                raise Exception()
            else:
                valid  = True
        except ValueError:
            print("Invalid input")
        except Exception:
            print("Value must be at least %s" % min)
    return n

def show_presets():
    print("----------------")
    print("Available presets:\n")
    for i in PRESETS.keys():
        print(i)

"""
Main program loop
"""
while True:
    welcome_message()
    commands()
    connectivities = connectivity_input()

    #for debugging purposes
    #print(connectivities)

    H = generate_hamiltonian(connectivities)
    evalues, evectors = np.linalg.eig(H)
    energies = get_energies(evalues)
    print_energies(energies)
    input("Press enter to continue...")
exit()
