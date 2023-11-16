# Dictionary functions
student_details = {"xyz": 100, "pqr": 200, "def": 167, "year": 2034, "Loc": "earth", "age":45}

# Remove items from dictionary using pop(key)
student_details.pop("def")
print(student_details)

# Delete specific item with the help of key
del student_details["Loc"]
print(student_details)

# Copy dictionaries
new_dictionary = student_details
print(new_dictionary)

# Copy using copy()
new_dictionary1 = new_dictionary.copy()
print(new_dictionary1)

# Use clear() to empty the dictionary
print(student_details.clear())

