import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	a = np.asarray(a) 
	flat = np.array(a.reshape(-1))  
	n, m  = new_shape
	if(len(flat) != n * m):
		return []
	return flat.reshape(new_shape).tolist() 