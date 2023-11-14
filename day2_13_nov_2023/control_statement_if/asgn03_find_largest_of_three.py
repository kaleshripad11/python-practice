# Program to find largest of two numbers
x, y, z = int(input("Enter first number : ")), int(input("Enter second number : ")), int(input("Enter third number : "))

if (x > y) & (x > z):
    print("The number {} is greater than the number {} & number {}!!".format(x,y,z))
elif (y > x) & (y > z):
    print("The number {} is greater than the number {} & number {}!!".format(y, x, z))
else:
    print("The number {} is greater than the number {} & number {}!!".format(z, x, y))
