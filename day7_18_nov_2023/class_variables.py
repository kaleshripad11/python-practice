# The variables which are created inside the class, called as class variables.
# These can't be accessed directly inside methods. Have to use 'self' keyword.
# Keyword 'self' can also be used to differentiate between local variables inside class & variables outside class


class ClassVariableDemo:
    x,y = 10,20     # Class variables. Can be called using self keyword. Ex. self.x

    def sum(self):
        print(self.x+self.y)

    def diff(self):
        print((self.x**4)-(self.y**3))


cvd = ClassVariableDemo()
cvd.sum()
cvd.diff()
