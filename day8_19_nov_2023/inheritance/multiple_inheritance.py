class Parent1:
    x = 100

    def parent_function1(self):
        print(self.x)


class Parent2:
    y, x = 90, 19

    def parent_function2(self):
        print(self.x+self.y)


class Child(Parent2, Parent1):
    def print_details(self):
        print(self.y - self.x)


c1 = Child()
c1.print_details()
c1.parent_function2()
c1.parent_function1()