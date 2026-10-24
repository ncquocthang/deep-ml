import numpy as np

def kernel_function(x1, x2):
	return np.sum(np.asarray(x1) * np.asarray(x2)) 
