import os
import ast
import sys
import configparser
from typing import Dict
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Dict


class Singleton(type):
    _instances: Dict = {}

    # Each of the following functions use cls instead of self
    # to emphasize that although they are instance methods of
    # Singleton, they are also *class* methods of a class defined
    # with Singleton
    def __call__(cls, *args, **kwargs):
        if cls not in Singleton._instances:
            Singleton._instances[cls] = super().__call__(*args, **kwargs)
        return Singleton._instances[cls]

    def clear(cls):
        try:
            del Singleton._instances[cls]
        except KeyError:
            pass


@dataclass
class Config(metaclass=Singleton):
    """
    Class which contains our configuration. Once initialized, it cannot be changed, as it is a singleton.
    """
    param1 : str
    param2 : int
    project_path : str

    def __post_init__(self):
        """
        Checks if paths are specified correctly (i.e. absolute paths, and if needed builds up absolute paths)
        """

    def __init__(
        self,
        config_path: str= "",
        param1 = None
    ):
        """
        Initialize configuration object. Configuration is read in from the path specified by the config_path
        argument.
        """

        if config_path:
            if os.path.isfile(config_path):
                config = configparser.ConfigParser()
                config.read(config_path)
                for section in config.sections():
                    for key in config[section]:
                        setattr(self, key, ast.literal_eval(config[section][key]))

        if param1:
            self.param1 = param1

        self.__post_init__()
