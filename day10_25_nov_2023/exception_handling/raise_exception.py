n1 = int(input("Enter first number : "))


def compare_number(a):
    if a<0:
        raise ValueError("Please enter value greater than zero")
    if a=='':
        raise ValueError("Please enter numbers only")



print(compare_number(n1))

