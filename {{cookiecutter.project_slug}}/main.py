from config_example import print_param1
from config import Config


if __name__ == "__main__":
    c = Config("./config.ini", param1="overwrite value")

    print(c.param1)
    print(c.param2)
    print(c.project_path)

    print_param1()




