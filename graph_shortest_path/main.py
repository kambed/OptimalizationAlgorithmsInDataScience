import logging

from graph_shortest_path.algorithms.shortest_path import ShortestPath
from graph_shortest_path.helper.argument_helper import ConfigHelper
from graph_shortest_path.helper.data_csv_helper import DataCsvHelper
from graph_shortest_path.helper.logging_helper import LoggingHelper

if __name__ == '__main__':
    debug = False
    end = None
    try:
        debug = ConfigHelper.get_bool_argument("debug")
    except ValueError:
        pass
    LoggingHelper.setup_logging(debug)
    start = ConfigHelper.get_argument("from")
    try:
        end = ConfigHelper.get_argument("to")
    except ValueError:
        pass

    df = DataCsvHelper.read_csv()
    paths = ShortestPath(df).get_shortest_path(start)
    logging.debug("================================")
    logging.info("Shortest paths:")
    for path in paths:
        if path[2] and (path[1] == end or not end):
            logging.info(f"{'->'.join(path[2])}->{path[1]} = {path[0]}")