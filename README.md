# Exercise 1: General Hückel Solver
Program to find Hückel molecular orbital energies and their degeneracies for π systems of arbitrary molecules made up of one element, with all atoms equidistant. 
To launch the program, run `main.py`

## Available molecule input modes
* `linear`      Prompts for an input of number of atoms. Generates orbital energies for a linear polyene or equivalent.
* `cyclic`      Prompts for an input of number of atoms. Generates orbital energies for a cyclic polyene or equivalent.
* `presets`     Displays a list of available preset molecules, including some common polyenes, platonic solids and fullerene.
* `custom`      Allows for specifying custom connectivity between atoms. 
 ### Sub-commands in custom mode
 * `add`        Add a bond between 2 atoms
 * `remove`     Remove an existing bond between 2 atoms
 * `bonds`      Displays a list of all current bonds
 * `done`       Completes the molecule and generates orbital energies

## Notes
* Energies are expressed in the form 'a + x b' where 'a' = α, the energy of an atomic orbital and 'b' = β, the energy of interaction between adjacent atomic orbitals. 
* Due to inaccuracies introduced by the numerical methods used in this program, energies are considered to be degenerate if they are equal to 12 decimal places. This may lead to non-degenerate orbitals being considered degenerate in the case of complex systems with multiple energy levels that lie close together in value. 