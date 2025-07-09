import time
from functools import reduce

def measure_time(func):
    def wrapper(x):
        start_time = time.time()
        result = func(x)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Operation time: {elapsed_time:.10f} seconds")
        return result
    return wrapper

@measure_time
def acronym(x):
    x = x.split()
    return reduce(lambda acc, word: acc + word[0].upper(), x, "")
print(acronym("portable network graphics"))

# # Get the input
# string = input("Enter a text: ").split()

# # Call acronym and get the result along with operation time
# result, elapsed_time = acronym(string)

# # Print results in the desired format
# print(f"Acronym: {result}")
# print(f"Operation time: {elapsed_time:.10f} seconds")