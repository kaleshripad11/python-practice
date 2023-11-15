# Python tuples :
# Collection of ordered items
# Immutable(Modification not allowed)
# Created with round brackets

tuplez = (1, 2, " ", 300.5, 0, 23, 89, 21, 9, 10, 2)
print(tuplez)

# Access tuple items
print(tuplez[1])        # Left to right index starts from 0
print(tuplez[-2])       # Right to left index starts from -1

# Reverse tuple
print(tuplez[::-1])

# Slicing of tuples
print(tuplez[2:5])
print(tuplez[-7:-2])

# We can modify tuples => First convert tuple to list > Perform modification on List > Again convert the list back
tuple_to_list = list(tuplez)
tuple_to_list.append(100)
print(tuple(tuple_to_list))

# Iterate tuples using loops
for i in tuplez:
    print(i)

# Check existence of given item in tuples
if 89 in tuplez:
    print("The number 89 found at index {}".format(tuplez.index(89)))

# Copy tuples
new_tuple = tuplez
print(new_tuple)

# Concatenation of tuples
print(tuplez+new_tuple)

# Compare tuples
print("Are tuples equal? => ", tuplez == new_tuple)