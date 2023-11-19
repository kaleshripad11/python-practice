class A:
    x, y = 10, 20

    def first_method(self):
        print(self.x + self.y)


class B(A):
    z = 2

    def second_method(self):
        print((self.x + self.y)/self.z)


class C(B):
    a = 49

    def third_method(self):
        print(self.x + self.y + self.z + self.a)


c = C()
c.second_method()
c.first_method()
c.third_method()
