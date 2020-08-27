from config import Config
import ast
if __name__ == "__main__":
    c = Config(env='DEFAULT')
    print(c)
    print(c.my_list)
    print(c.my_second_list)

