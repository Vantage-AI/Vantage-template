from config_example import print_param1
from config import Config


if __name__ == "__main__":
    c = Config(config_path='/Users/guidotournois/Projects/Vantage-template/{{cookiecutter.project_slug}}/config.ini',
               param1 = 'overwrite 1')

    print(c.param1)
    print(c.param2)
    print(c.project_path)

    c = Config(config_path='/Users/guidotournois/Projects/Vantage-template/{{cookiecutter.project_slug}}/config.ini',
               param1='overwrite 2')

    print(c.param1)
    print(c.param2)
    print(c.project_path)

    print_param1()



