import time
from functools import reduce

def measure_time(func):
    def wrapper(x):
        global elapsed_time
        start_time = time.time()
        result = func(x)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return result
    return wrapper

@measure_time
def acronym(x):
    x = x.split()
    return reduce(lambda acc, word: acc + word[0].upper(), x, "")
print(acronym("portable network graphics"))
print(acronym("information technology"))
print(f"Operation time: {elapsed_time:.10f} seconds")