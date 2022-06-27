import time


from unicodedata import name 

# 1. 

# Swap two variables in python with third variables

first_var = 5
second_var = 7

print("Value of variables before swapping", first_var, second_var)

temp_var = first_var
first_var = second_var
second_var = temp_var

print("Value of variables after swapping", first_var, second_var)

# 2. 

# Swap two variables in python without third variables


first_var = 5
second_var = 7

print("Value of variables before swapping", first_var, second_var)

first_var, second_var = second_var, first_var

print("Value of variables after swapping", first_var, second_var)

# 3.

# Calculate the time taken by function using decorator in python

'''
calculate_function_execution_time function measure the execution time of provided function as an argument
'''

def calculate_function_execution_time(function):
    def wrapper_function(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        end_time = time.time()
        print(f'Function {function.__name__} executed in {(end_time-start_time)}s')
    return wrapper_function


@calculate_function_execution_time
def do_add(*args, **kwargs):
    '''
    do_add function returns the sum of all arguments provided
    '''
    print("Addition of all provided arguments are", sum(args))

do_add(3, 4, 5)

# 4.

# Calculate number of times function called using decorator in python

'''
counter_function calculate the number of times function called provided in argument
'''

def counter_function(func):
    global func_calls
    func_calls = 0
    def wrapper_function(*args, **kwargs):
        global func_calls
        func_calls += 1
        func(*args, **kwargs)
        print(f'Function named {func.__name__} called {func_calls} number of times')
    return wrapper_function

@counter_function
def do_add(*args, **kwargs):
    '''
    do_add function returns the sum of all arguments provided
    '''
    print("Addition of all provided arguments are", sum(args))

if __name__ == "__main__":
    do_add(1)
    do_add(1, 2)
    do_add(1, 2, 3)