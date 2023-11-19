class A:
    x = 200
    def dummy_function(self):
        print("This is class A")


class B(A):
    x = 100
    def dummy_function(self):
        print("This is class B")
        print(self.x)
        print(super().x)
        super().dummy_function()


b = B()
b.dummy_function()
