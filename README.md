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
