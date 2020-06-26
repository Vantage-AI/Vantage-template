from config import Config
from test.test import read_data

if __name__ == "__main__":
    c = Config(env='DEVELOPMENT')
    read_data()
