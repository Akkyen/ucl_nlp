## Class struct to store parameters
from common.utils import init_arg_parser

class Parameters():
    def __init__(self):
        arg_parser = init_arg_parser()
        return arg_parser

train_param = Parameters()
print(train_param.seed)

