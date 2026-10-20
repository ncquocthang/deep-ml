
import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	y = np.asarray(y) 
	value, count = np.unique(y, return_counts = True) 
	count = count / len(y) 
	val = 1 - np.sum(count * count) 
	return round(val,3)