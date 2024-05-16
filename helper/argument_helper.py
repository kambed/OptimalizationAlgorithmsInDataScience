import logging
from enum import Enum
import json


class ConfigHelper:
    @staticmethod
    def get_enum_argument(arg_name, enum_class):
        if not issubclass(enum_class, Enum):
            raise ValueError("Second argument must be an Enum class")

        value = ConfigHelper.get_argument(arg_name)
        try:
            return enum_class[value]
        except KeyError:
            raise ValueError(f"Invalid value {value} for argument {arg_name}")

    @staticmethod
    def get_int_argument(arg_name):
        value = ConfigHelper.get_argument(arg_name)
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"Invalid value {value} for argument {arg_name}")

    @staticmethod
    def get_float_argument(arg_name):
        value = ConfigHelper.get_argument(arg_name)
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Invalid value {value} for argument {arg_name}")

    @staticmethod
    def get_bool_argument(arg_name):
        value = ConfigHelper.get_argument(arg_name)
        try:
            return bool(value)
        except ValueError:
            raise ValueError(f"Invalid value {value} for argument {arg_name}")

    @staticmethod
    def get_list_argument(arg_name):
        value = ConfigHelper.get_argument(arg_name)
        try:
            return list(map(lambda x: float(x), value.split(",")))
        except ValueError:
            raise ValueError(f"Invalid value {value} for argument {arg_name}")

    @staticmethod
    def get_argument(arg_name):
        with open("resources/config.json") as f:
            arguments = json.load(f)
            if arg_name not in arguments:
                raise ValueError(f"Missing argument {arg_name} in config.json")

            print(f"{arg_name}: {arguments[arg_name]}")

            return arguments[arg_name]

    @staticmethod
    def check_if_argument_exists(arg_name):
        with open("resources/config.json") as f:
            arguments = json.load(f)
            if arg_name not in arguments:
                return False
            return True