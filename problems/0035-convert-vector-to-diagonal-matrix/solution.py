import numpy as np

def make_diagonal(x):
	x = np.asarray(x) 
	res = np.zeros((len(x), len(x)))
	res[np.arange(len(x)), np.arange(len(x))] = x 
	return res 