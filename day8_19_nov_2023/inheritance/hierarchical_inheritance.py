class MainParent:
    a, b = 25, 3

    def parent_function(self):
        print(self.a>self.b)


class Child1(MainParent):
    c = 100

    def who_is_greater_among_three(self):
        if self.a > self.b & self.a > self.c:
            print("Greater is : ", self.a)
        elif self.b > self.a & self.b > self.c:
            print("Greater is : ", self.b)
        else:
            print("Greater is : ", self.c)


class Child2(MainParent):
    def print_average(self):
        print((self.a + self.b)/2)


c1 = Child1()
c2 = Child2()

c1.parent_function()
c2.parent_function()
c1.who_is_greater_among_three()
c2.print_average()