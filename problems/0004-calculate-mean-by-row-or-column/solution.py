import numpy as np  

def calculate_matrix_mean(matrix: list[list[float]], mode: str):
    matrix = np.asarray(matrix) 
    if mode == 'row': 
        matrix = matrix.T
    return np.sum(matrix / matrix.shape[0] , axis = 0, dtype= float).tolist() 