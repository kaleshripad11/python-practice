# Dictionaries :
# Values are stored in key-> value format
# Unordered and indexed collections
# Values are again stored with {} braces
# Keys are unique, while values can be duplicate
# example : student_details = {"xyz": 100}, "pqr": 200}

student_details = {"xyz": 100, "pqr": 200, "def": 167}
print(type(student_details))        # <class 'dict'>
print(student_details)

# Get list of keys
print(student_details.keys())

# Access items in the dictionary using keys
print(student_details["def"])

# Access items in the dictionary using get()
print(student_details.get("pqr"))

# Change values in dictionary
student_details["pqr"] = 20
print(student_details)

# Iterating through the dictionaries
print("Printing only dictionary values")
for i in student_details.values():
    print(i)

print("Printing dictionary values")
for i in student_details:
    print(student_details[i])

print("Printing dictionary keys")
for i in student_details:
    print(i)

# Print keys & values in a dictionary using item()
print("Printing keys & values of a dictionary")
print("Key", " ==> ", "Values")
for i,j in student_details.items():
    print(i, " ==> ", j)

# Check existence of keys in dictionary
print("tux" in student_details)

# find items count in dictionary
print(len(student_details))

# Add items to dictionary
student_details["batch"] = 2023
print(student_details)