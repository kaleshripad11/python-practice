# IF - Else Condition is an extension of if statement. It will move the control as per the condition
# If condition is not satisfied, then control will be moved to else block and all statements in else block will be
# executed

# Normal If Else Syntax
age = int(input("Enter your age : "))
if age <= 30:
    print("Congrats!, Your age is {} and its a valid age for this government exam".format(age))
else:
    print("Sorry!, Your age is {} and its not a valid age for this government exam".format(age))

# Ternary Way
print("Congrats! you are eligible".format(age)) if age <= 30 else print("Sorry!, you are not eligible".format(age))
{print(10+2),print(200/5)} if age <= 30 else print("Sorry!, you are not eligible".format(age))
