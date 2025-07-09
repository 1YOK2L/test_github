import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Get the start time
        result = func(*args, **kwargs)  # Call the original function
        end_time = time.time()  # Get the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f"Operation time: {elapsed_time:.10f} seconds")  # Print the elapsed time
        return result
    return wrapper

@measure_time
def acronym(x):
    for i in range(len(x)):
        a = (x[i][0]).upper()
        print(a, end = "")
    print()
string = input("Enter a text: ").split()
acronym(string)