# Functions are the set of re-usable statements
# In python functions are defined with "def" keyword

# Normal function
def function_demo():
    print("Hey, this is a python function!!!")


function_demo()


# Parameterized function
def parameterized_function(name):
    print("Hello ", name)


parameterized_function("Python")


# print sum of two numbers
def sum_of_two_numbers(a, b):
    print(a+b)


sum_of_two_numbers(10, 5)


# Python functions can return multiple values in the form of tuples
def return_demo(x, y, z):
    return x, y, z


print(return_demo(10,5,20))