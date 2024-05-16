import logging

from algorithms.bayes_laplace_model import BayesLaplaceModel
from algorithms.enum.algorithm import Algorithm
from algorithms.hurwicz_model import HurwiczModel
from algorithms.optimistic_model import OptimisticModel
from algorithms.savage_model import SavageModel
from algorithms.walds_maximin_model import WaldsMaximinModel
from helper.argument_helper import ConfigHelper
from helper.data_csv_helper import DataCsvHelper
from helper.logging_helper import LoggingHelper


def create_algorithm():
    algorithm_enum = ConfigHelper.get_enum_argument("algorithm", Algorithm)
    if algorithm_enum == Algorithm.WALDS_MAXIMIN:
        return algorithm_enum, WaldsMaximinModel()
    elif algorithm_enum == Algorithm.OPTIMISTIC:
        return algorithm_enum, OptimisticModel()
    elif algorithm_enum == Algorithm.HURWICZ:
        precaution = ConfigHelper.get_float_argument("precaution")
        return algorithm_enum, HurwiczModel(precaution)
    elif algorithm_enum == Algorithm.BAYES_LAPLACE:
        probability = ConfigHelper.get_list_argument("probability")
        return algorithm_enum, BayesLaplaceModel(probability)
    elif algorithm_enum == Algorithm.SAVAGE:
        return algorithm_enum, SavageModel()
    else:
        raise NotImplementedError(f"Algorithm {algorithm_enum.name} not found!")


if __name__ == '__main__':
    debug = False
    try:
        debug = ConfigHelper.get_bool_argument("debug")
    except ValueError:
        pass
    LoggingHelper.setup_logging(debug)

    df = DataCsvHelper.read_csv()
    algorithm, implementation = create_algorithm()
    logging.info(f"====={algorithm.name}=====")
    solution = implementation.solve(df)
    logging.debug(solution)
    logging.debug(f"==================")
    if algorithm == Algorithm.SAVAGE:
        indexes = solution[solution == solution.min()]
    else:
        indexes = solution[solution == solution.max()]
    logging.info("Indexes:")
    for index in indexes.index:
        logging.info(f"- {index}")
    logging.info(f"==================")