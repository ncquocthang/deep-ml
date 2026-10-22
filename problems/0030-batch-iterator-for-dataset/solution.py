import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    n_samples = X.shape[0]
    
    for i in range(0, n_samples, batch_size):
        begin = i
        end = i + batch_size
        
        if y is not None:
            yield [X[begin:end].tolist(), y[begin:end].tolist()]
        else:
            yield X[begin:end].tolist()