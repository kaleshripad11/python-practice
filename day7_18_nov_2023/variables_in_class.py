# Keyword 'self' can also be used to differentiate between local variables inside class & variables outside class
# Also globals() can be used to differentiate the variables
# Syntax for globals() => globals()['var_name']

x, y = 100, 300     # Global Variables


class AllVariables:
    z = 20
    x, y = 3, 4

    def sum(self):
        print(self.z + x + y)

    def diff(self):
        print(self.y - self.x)

    def print_sum_of_global_vars(self):
        print(self.y - self.x)                  # Class local variables
        print(globals()['x']+globals()['y'])    # Global variables

    def parameterized_function(self,x, y):
        print(x < y)

av = AllVariables()
av.sum()
av.diff()
av.print_sum_of_global_vars()

av1 = AllVariables()
av1.parameterized_function(10,5)
av.parameterized_function(1,5)