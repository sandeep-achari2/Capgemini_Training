import time  # Import time module for execution time measurement
import functools  # Import functools to preserve function metadata

def log_execution(func):  # Define a decorator that takes a function as input
    """A custom decorator to log function calls and execution time."""
    
    @functools.wraps(func)  # Preserves function metadata (name, docstring)
    def wrapper(*args, **kwargs):  # Define an inner function to modify behavior
        start_time = time.time()  # Record the start time before executing the function
        result = func(*args, **kwargs)  # Call the actual function with its arguments
        end_time = time.time()  # Record the end time after function execution
        
        print(f"Function '{func.__name__}' called with arguments: {args}, {kwargs}")
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        
        return result  # Return the original function's result
    
    return wrapper  # Return the modified function

@log_execution  # Apply the decorator
def add_numbers(a, b):
    """Function to add two numbers."""
    time.sleep(1)  # Simulate some processing delay
    return a + b
result = add_numbers(5, 10)
print("Result:", result)



