import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	a = np.asarray(a) 
	n_rol_a, n_col_a = np.shape(a) 
	len_b = len(b) 
	b = np.asarray(b) 
	if n_col_a != len_b: 
		return -1 
	return np.dot(a,b).tolist() 
