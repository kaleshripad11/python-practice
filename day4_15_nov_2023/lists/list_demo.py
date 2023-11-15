"""
List :
It is collection type.
It is ordered and those are changeable
List values are enclosed in [] brackets.
It is mutable.
It can hold any type of data. Ex. demo_list = [1, 10.5, "Python", True]
Empty lists can be created using list() function
"""
programming_lst = ["Java", 17, "Python", 3.12, "pHp", 7]
print("Programming list: ", programming_lst, ",OOps Programming: ", programming_lst[0], ",Version: ",programming_lst[1])

# List slicing
list1 = [1, 3, 4, 8, 100, 200, 70]
print("Slicing : ", list1[2:4])

# List mutation[List items can be changed once list is defined]
print("Original List : ", list1)
list1[4], list1[5] = 30, 35
print("Updated List : ", list1)

# Print list items using loop
for i in list1:
    print(i)

# Check if an item exists in the list or not
number = int(input("Please enter a numer to check its presence in the list : "))
if number in list1:
    print("Your entered number {} is found at {}".format(number,list1.index(number)))
else:
    print("Your entered number does not exists in the list!!!")