# Python provides different ways to print the output
# Syntax 1: print("Msg1 %d, Msg2 %s, Msg3 %g" %(var1, var2, var3)
# In above syntax - %d, %g & %s represents int, float & string types
# Syntax 2: print("Msg1 {}, Msg2 {}, Msg3 {}".format(var1, var2, var3)

name, age, address, marks = 'xyz', 20, 'Test Address', 87.60
print("Name : %s, Age : %d, Address : %s, Marks : %g" %(name,age,address,marks))
print("Name : {}, Age : {}, Address : {}, Marks : {}".format(name,age,address,marks))
