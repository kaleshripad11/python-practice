"""
1.Strings are immutable in python. It means we can not change its contents
"""
x = "Welcome"
print(x, "",id(x))
x = "Welcome to python"
print(x, "",id(x))

# String slicing
print(x[2:14])
print(x,"",x[::-1])      # Reverse(Mirror Image) the string. Output : Welcome to python  nohtyp ot emocleW

# String functions
# ord() => Returns ascii code of the character
print(ord('B'))         # Output: 66

# chr() => Returns character value for provided ascii code
print(chr(90))          # Output: Z

# min() & max() => can also be used with strings. It will return the character based on its ascii value
print(min("Python"))
print(max("Python"))

# String operators => in, not in
# Operator : in => it will return true if the given string/value exists in given string/variable
string_demo = "Welcome to python"
print("py" in string_demo)         # Output: True
print(" " not in string_demo)      # Output: False

# String comparisons
print("Python" == "Java")       # Output: False
print("Python" == "Python")
print("Python" != "Java")
print("Python" <= "Java")

# String testing functions
greeter = 'Hello'
print(string_demo.isalnum())    # Return True if string consists of alphanumerics
print(greeter.isalpha())    # Return True if string consists of only alphabets
print("2023".isdigit())     # Return True if string consists of digits only
print("python".islower())   # Return True if string is in lower case
print("PYTHON".isupper())   # Return True if string is in upper case
print("  ".isspace())       # Return True if string consists of only spaces
print(string_demo.endswith("on"))
print(string_demo.startswith("yth"))
print(string_demo.find("x"))
print(string_demo.count("e"))

# String case conversion functions
dummy_string = "pYthOn woRld"
print(dummy_string.title())
print(dummy_string.swapcase())
print(dummy_string.capitalize())
print(dummy_string.casefold())
print(dummy_string.replace("o","i"))






















