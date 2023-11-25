n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))

try:
    print(n1/n2)
except ZeroDivisionError:
    print("Can not divide any number by zero")
except ArithmeticError:
    print("Please enter a valid number")
else:
    print("This is executed only when exception is occurred")
finally:
    print("This will always executed")