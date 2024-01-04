import numpy as np

# Deux tableaux NumPy
array1 = np.array([[1, 2, 3],
                   [4, 5, 6]])

array2 = np.array([[7, 8, 9],
                   [10, 11, 12]])

# Utilisation de np.vstack pour les empiler verticalement
stacked_array = np.vstack((array1, array2))

print("Tableau 1:")
print(array1)
print("\nTableau 2:")
print(array2)
print("\nTableau empilé verticalement:")
print(stacked_array)
