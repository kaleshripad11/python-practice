# Variables are dynamic in nature in python
# It means that - we do not need to specify the variable type while creating a variable
# Based on the value assigned the datatype will be decided at runtime
# Also python allows programmers to create variables in different ways
# These are some types in python :
# Numeric types : int, float
# Booleans : True, False
# String : str
# Others : List, Tuples
# We can determine the type of variables using built-in function called as 'type(variable)'

# All Type Variables Examples
a = 10
b = 10.1
d = "hey there"
e = True
f = [10, "12"]
g = (100, 200)

print("Value of 'a' : ", a, ", and it's type is : ", type(a))
print("Value of 'b' : ", b, ", and it's type is : ", type(b))
print("Value of 'd' : ", d, ", and it's type is : ", type(d))
print("Value of 'e' : ", e, ", and it's type is : ", type(e))
print("Value of 'f' : ", f, ", and it's type is : ", type(f))
print("Value of 'g' : ", g, ", and it's type is : ", type(g))

# Define multiple variables in single line
a, b, c = 10, "Hello World", False
print("Value of 'a' :", a, ", Value of 'b' :", b, ", Value of 'c' :", c)

# Define multiple variables having same value in one line
a = b = c = 200
print("Value of 'a' :", a, ", Value of 'b' :", b, ", Value of 'c' :", c)

# Swap two numbers easily
x, y = 10, 5
print("Initial values of x & y : ", x, y)
x, y = y, x
print("Swapped values of x & y : ", x, y)

# Change the types of variables once they are declared
y = 10.5    # Initial value of Y was 5, after swapping it became 10, and now we again updated it to float 10.5
print("Value of 'y' : ", y)
