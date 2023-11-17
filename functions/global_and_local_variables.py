# Python variables has two scopes => Global & Local
# Global => Created out-side of a function/code block, can be accessed from anywhere
# Local => Created in-side the function body. Can be accessed only inside the function
# If a program contains similar variable at global and local level, first preference will be given to local variable
# The global variables can be accessed inside function using keyword "global"
# The global keyword changes scope of the variable hence, using it global variables can be defined inside function also
# To do this, first define similar variable with global keyword and then initialize the value.
# Ex : global x
# x = 10


glob_var = "This is a global variable"


def local_var_function():
    loc_var = "This is a local variable"
    print(glob_var)
    print(loc_var)


print(local_var_function())
print("Global Variable : ", glob_var)
# print("Local Variable : ", loc_var) => Invalid statement as loc_var is not global

x = 10


def similar_as_x():
    x = 20
    print(x)


similar_as_x()


# Define global variables inside function
def global_in_function():
    global y
    y = 89
    print(y)


global_in_function()


