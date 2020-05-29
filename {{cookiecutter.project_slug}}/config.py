import os
import ast
import configparser
from typing import Dict
from dataclasses import dataclass


class Singleton(type):
    """
    Make sure that whenever a config object is initialized, we obtain the same instance.

    Each of the following functions use cls instead of self to emphasize that although they are instance methods of
    Singleton, they are also *class* methods of a class defined with Singleton
    """
    __instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in Singleton.__instances:
            Singleton.__instances[cls] = super().__call__(*args, **kwargs)
        return Singleton.__instances[cls]

    def clear(cls):
        try:
            del Singleton.__instances[cls]
        except KeyError:
            pass


@dataclass
class Config(metaclass=Singleton):
    """
    Class which contains our configuration. Once initialized, it cannot be changed, as it is a singleton.
    """
    param1 : int
    data_path : str

    def __init__(
        self,
        env: str = "DEVELOPMENT",
        config_path: str = "./config.ini",
    ):
        """
        Initialize configuration object. Configuration is read in from the path specified by the config_path
        argument.
        """

        if config_path:
            if os.path.isfile(config_path):
                config = configparser.ConfigParser()
                config.read(config_path)
                for key in config[env]:
                    setattr(self, key, ast.literal_eval(config[env][key]))
