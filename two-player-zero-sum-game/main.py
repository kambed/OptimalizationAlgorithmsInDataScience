import logging

import numpy as np

from helper.argument_helper import ConfigHelper
from helper.logging_helper import LoggingHelper
from helper.data_csv_helper import DataCsvHelper
from algorithms.walds_maximin import WaldsMaximinModel
from algorithms.dominated_strategies import remove_dominated_strategies

if __name__ == '__main__':
    debug = False
    try:
        debug = ConfigHelper.get_bool_argument("debug")
    except ValueError:
        pass
    LoggingHelper.setup_logging(debug)

    df, index_name = DataCsvHelper.read_csv()
    matrix = df.values
    logging.info(f"Game matrix:\n{matrix}")

    minimax, maximin, row_min, col_max = WaldsMaximinModel.solve(matrix)

    if minimax == maximin:
        logging.info(f"Game is solvable in clean strategies.")
        logging.info(f"Player A strategy: {np.argmax(row_min) + 1}")
        logging.info(f"Player B strategy: {np.argmin(col_max) + 1}")
    else:
        logging.info(f"Game is not solvable in clean strategies. LP model is needed.")

        reduced_matrix = remove_dominated_strategies(matrix)
        logging.info(f"Reduced matrix:\n{reduced_matrix}")
