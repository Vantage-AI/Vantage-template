"""Module to create global configuration class."""

import os
import ast
from configparser import ConfigParser
from typing import Dict, Any
from dataclasses import dataclass


class Singleton(type):
    """Make sure that whenever a config object is initialized, we obtain the same instance.

    Each of the following functions use cls instead of self to emphasize that although they are instance methods of
    Singleton, they are also *class* methods of a class defined with Singleton
    """
    __instances: Dict = {}

    def __call__(cls, *args, **kwargs):
        """Get instance of singleton."""
        if cls not in Singleton.__instances:
            Singleton.__instances[cls] = super().__call__(*args, **kwargs)
        return Singleton.__instances[cls]

    def clear(cls: Any) -> None:
        """Remove all singletons."""
        try:
            del Singleton.__instances[cls]
        except KeyError:
            pass


@dataclass
class Config(metaclass=Singleton):
    """Class which contains our configuration.

    Can only be initialized once. Everytime it is loaded, one receives the same instance, as it is a singleton.
    """
    param: int
    data_path: str
    project_root: str

    def __init__(
        self,
        env: str = "DEVELOPMENT",
        config_path: str = "./config.ini",
        project_root: str = None
    ):
        """Configuration is read in from the path specified by the config_path argument."""
        if project_root:
            self.project_root = project_root
        else:
            self.project_root = os.path.dirname(os.path.abspath(__file__))

        if not os.path.exists(self.project_root):
            raise FileNotFoundError("The path given as project root does not exist")
        if not os.path.isdir(self.project_root):
            raise NotADirectoryError("The path given is not a directory, but a file path")

        if config_path:
            if os.path.isfile(config_path):
                config = ConfigParser()
                config.read(config_path)

                env_keys = [key.rsplit('[')[0].strip() for key in config[env].keys()]
                duplicate_keys = (set([x for x in env_keys if env_keys.count(x) > 1]))
                defaults = list(config.defaults())

                _ = [config.defaults().pop(key) for key in defaults if key.rsplit('[')[0].strip() in duplicate_keys]

                for key in config[env]:
                    if '[float]' in key or '[double]' in key:
                        setattr(self, key.rsplit('[')[0].strip(), float(config[env][key]))
                        continue
                    if '[int]' in key:
                        setattr(self, key.rsplit('[')[0].strip(), int(config[env][key]))
                        continue
                    if '[path]' in key:
                        config[env][key] = config[env][key].replace('${project_root}', self.project_root)
                    setattr(self, key.rsplit('[')[0].strip(), ast.literal_eval(config[env][key]))
            else:
                raise FileNotFoundError(f'No config file at location {config_path} has been found')
        else:
            raise ValueError("Please provide a config path")

    def __str__(self) -> str:
        """Return string representation."""
        return "\n".join([f"{key}: {value}" for key, value in self.__dict__.items()])
