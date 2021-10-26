def num_atoms (mass, weight = 196.97):
    mol = mass/weight
    number_of_atoms = mol*(6.022*(pow(10,23)))
    
    print("The number of atoms is: ", number_of_atoms)

num_atoms(10)
num_atoms(10, 12.001)
num_atoms(10, 1.008)