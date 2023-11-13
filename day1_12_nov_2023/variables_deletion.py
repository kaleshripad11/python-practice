# In python, a variable can be deleted using 'del' keyword
# Check below example
a = 100
b = "Python"

print("Value of a : ", a)
print("Value of b : ", b)

del b   # Deleted the variable b
print("Value of a : ", a)   # Statements after this will not be executed and programme will throw "NameError"
print("Value of b : ", b)

c = 10.5
print("Value of c : ", c)