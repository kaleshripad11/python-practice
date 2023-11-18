# Constructors in python.
# In python, constructors are defined with "__init__(self)".
# Constructors does not return any value.
# It can also take arguments.
# When object is created for a class, the constructor will be invoked.

class PythonConstructors:
    def __init__(self):
        print("This is a default constructor")

    def parameterized_function(self,x, y):
        print(x < y)


pyconst = PythonConstructors()
pyconst.parameterized_function(10,4)