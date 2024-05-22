import logging

import numpy as np


def remove_dominated_strategies(matrix):
    rows_to_remove = set()
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[0]):
            if i != j and all(matrix[i, k] <= matrix[j, k] for k in range(matrix.shape[1])):
                rows_to_remove.add(i)

    logging.debug(f"Rows to remove: {rows_to_remove}")
    matrix = np.delete(matrix, list(rows_to_remove), axis=0)

    cols_to_remove = set()
    for i in range(matrix.shape[1]):
        for j in range(matrix.shape[1]):
            if i != j and all(matrix[k, i] >= matrix[k, j] for k in range(matrix.shape[0])):
                cols_to_remove.add(i)

    logging.debug(f"Cols to remove: {cols_to_remove}")
    matrix = np.delete(matrix, list(cols_to_remove), axis=1)

    return matrix
