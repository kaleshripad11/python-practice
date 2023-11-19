# In python method overloading can be achieved through use of keyword arguments

class A:
    x,y = 10, 2

    def arithmatics(self, x = 10, y = 20):
        print(x/y)


a = A()
a.arithmatics()
a.arithmatics(x=250)
a.arithmatics(x=10,y=4)