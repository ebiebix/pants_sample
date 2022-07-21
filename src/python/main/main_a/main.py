from lib.lib_a.sample import sample
from lib.lib_a.log import set_logging_basic_config

if __name__ == "__main__":
    set_logging_basic_config("INFO")
    print("hello world!")
    sample()
