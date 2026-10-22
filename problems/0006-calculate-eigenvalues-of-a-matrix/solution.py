import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	mat = np.asarray(matrix) 

	eigenvalues = np.linalg.eigvals(mat) 
	sorted_eig = sorted([float(x) for x in eigenvalues], reverse = True) 
	return sorted_eig