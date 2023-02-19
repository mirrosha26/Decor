import os
import datetime

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):

            result = old_function(*args, **kwargs)

            with open(path, "a") as file:
                file.write(f'{datetime.datetime.now()}; {old_function.__name__}; {args} and {kwargs}; {result}\n')
            return result
        return new_function
    return  __logger
