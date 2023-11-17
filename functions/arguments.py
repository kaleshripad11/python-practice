# In python, two types of parameters can be provided to a function
# Positional Arguments
# Keyword Arguments

# Positional Arguments
# Positional Argument must appear before any keyword arguments
def positional_args_function(x, z, y):
    print(x, z, y)


positional_args_function(10, 20, 3)


# Keyword Arguments
def keyword_args_function(x, z, y):
    print(x, z, y)


keyword_args_function(x=100, y=2000, z=102)


# Default arguments
def default_args_function(x, y, z=True):
    print(x, y, z)


default_args_function(10, 20)


# Combination of positional & keyword arguments
def comb_of_positional_keyword_args(x, y, z=10):
    print(x, y, z)


comb_of_positional_keyword_args(10, 20, z=100)
