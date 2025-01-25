import numpy as np

A = np.array([
    [8, 5, 5, 5, 5, 5],  # Anan
        [8, 8, 7, 8, 7, 7],  # Bhucha
        [6, 9, 6, 6, 6, 6],  # Chandra
        [6, 6, 8, 6, 6, 6],  # Denchai
        [6, 6, 6, 6, 6, 6],  # Ekkamol
        [8, 8, 8, 8, 6, 8],  # Feungfa
])

B = np.array([5.69, 7.61, 6.81, 6.18, 6.33, 7.72])

X = np.linalg.solve(A, B)

print("Solution for X:")
print(X)
