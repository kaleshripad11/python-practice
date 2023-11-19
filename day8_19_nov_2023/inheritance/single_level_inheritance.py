# Acquiring variables & behaviors from parents into child classes

# Single level inheritance
class A:
    x, y = 10, 20
    def first_method(self):
        print(self.x + self.y)


class B(A):
    z = 2

    def second_method(self):
        print((self.x + self.y)/self.z)


b = B()
b.second_method()
b.first_method()