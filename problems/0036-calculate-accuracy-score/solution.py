import numpy as np

def accuracy_score(y_true, y_pred):
	y_true = np.asarray(y_true) 
	y_pred = np.asarray(y_pred) 
	return np.sum(np.where(y_true == y_pred, 1, 0)) / len(y_true) 