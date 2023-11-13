# In python inputs can be taken from command line/end users using function "input()"
# All the inputs taken using input() are of type 'str' in nature by default.
# In order to perform operations on values(ex. in case of numbers) typecasting is required
# For typecasting python provides functions like int(), float(), str()
a = int(input("A : "))
b = int(input("B : "))
print("Some of a & b : {} ".format(a+b))

a = input("A : ")
b = input("B : ")
print("Some of a & b : {} ".format(a+b))

a = input("A : ")
b = input("B : ")
print("Some of a & b : {} ".format(float(a) + float(b)))

