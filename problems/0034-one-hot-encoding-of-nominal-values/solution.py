import numpy as np 

def to_categorical(x, n_col= None): 
	if n_col is None: 
		n_col = np.max(x) + 1 
	n_rows = len(x) 
	one_hot = np.zeros((n_rows, n_col)) 
	one_hot[np.arange(n_rows), x] = 1.0 
	return one_hot 