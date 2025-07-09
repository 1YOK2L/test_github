import time
from functools import reduce

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Get the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Get the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        return result, elapsed_time  # Return both the result and elapsed time
    return wrapper

@measure_time
def acronym(x):
    # Use reduce to accumulate the first letter of each word
    return reduce(lambda acc, word: acc + word[0].upper(), x, "")

# Get the input
string = input("Enter a text: ").split()

# Call acronym and get the result along with operation time
result, elapsed_time = acronym(string)

# Print results in the desired format
print(f"Acronym: {result}")
print(f"Operation time: {elapsed_time:.10f} seconds")