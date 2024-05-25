from graph_shortest_path.algorithms.shortest_path import ShortestPath
from graph_shortest_path.helper.argument_helper import ConfigHelper
from graph_shortest_path.helper.data_csv_helper import DataCsvHelper
from graph_shortest_path.helper.logging_helper import LoggingHelper

if __name__ == '__main__':
    debug = False
    try:
        debug = ConfigHelper.get_bool_argument("debug")
    except ValueError:
        pass
    LoggingHelper.setup_logging(debug)

    df = DataCsvHelper.read_csv()
    ShortestPath(df).get_shortest_path("1")