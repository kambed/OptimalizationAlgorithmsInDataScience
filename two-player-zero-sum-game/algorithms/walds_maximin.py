import logging

import numpy as np


class WaldsMaximinModel:

    @staticmethod
    def solve(matrix):
        row_min = np.min(matrix, axis=1)
        col_max = np.max(matrix, axis=0)

        minimax = np.max(row_min)
        maximin = np.min(col_max)

        logging.debug(f"Row min: {row_min}")
        logging.debug(f"Col max: {col_max}")
        logging.debug(f"Minimax: {minimax}")
        logging.debug(f"Maximin: {maximin}")

        return minimax, maximin, row_min, col_max
