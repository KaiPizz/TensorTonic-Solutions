import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A = np.asarray(A)
    rows, cols = A.shape
    result = np.empty((cols, rows))
    for i in range(rows):
        for j in range(cols):
            result[j,i] = A[i,j]
    return result
    pass