# Get no of elements(length) in the list
lists = [10, 20.1, "Java", "Year - 2023", ascii("x"), 200, 35.8, True]
print("List : ", lists, ", Length : ", len(lists))

# append() => append the items at the end of lists
lists.append("Hey")
print(lists)

# insert() => Add itme at given index
lists.insert(3, "mysql")
print(lists)

# count(item) => Get occurrences count of 'item'
print(lists.count(10))

# Remove items from lists
# remove(item) => Remove items from list at given index
lists.remove("Java")
print(lists)

# Can also be used del keyword
del lists[2]
print(lists)

# pop(index) =>
lists.pop(5)
print(lists)

# clear() => Empty list
lists.clear()
print(lists)

# Copy lists
list_z = [10, 20.1, "Java", "Year - 2023", ascii("x"), 200, 35.8]
x = list_z.copy()
print(x)

# x = list(list_z)
x = list()
print(x)

# Concatenate lists
print(x+list_z)

# List concatenation using loop
for i in list_z:
    x.append(i)
print("Items in list 'x' : ", x)
