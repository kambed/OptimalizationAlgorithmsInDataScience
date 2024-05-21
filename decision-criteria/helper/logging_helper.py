import logging
import sys


class LoggingHelper:
    @staticmethod
    def setup_logging(debug):
        logging.basicConfig(
            format='%(message)s',
            level=logging.DEBUG if debug else logging.INFO,
            stream=sys.stdout
        )