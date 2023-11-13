# Unlike other programming languages, python also supports operators. Below are the some operators
# Arithmetic Operator [+, -, *, /, //, %, **]
# Relational Operators [>,<, >=, <=, !=, ==]
# Logical Operators [And, Or, Not]

# Arithmetic Operators
a,b=10,2
print("Sum of a & b : ",(a+b))
print("Dif of a & b : ",(a-b))
print("Div of a & b : ",(a/b))
print("Mul of a & b : ",(a*b))
print("Rem of a & b : ",(a%b))
print("Div of a & b : ",(a//b))
print("Exp of a & b : ",(a**b))

# Relational Operators[Always returns boolean values]
print("Is a > b ? : ", (a > b))     # True
print("Is a >= b ? : ", (a >= b))   # True
print("Is a != b ? : ", (a != b))   # True
print("Is a == b ? : ", (a == b))   # False
print("Is a < b ? : ", (a < b))     # False
print("Is a <= b ? : ", (a <= b))   # False

# Logical Operators
c, d = True, False
print(c and d)
print(c or d)
print((not(c)) and d)
print(c and not(d))
print(c or d)
print(not(c) and d)

# Concatenation operator [Plus(+)]
print(c+c)
print(c+d)
# print(c+'Python')   # Invalid statement, Only strings can be concatenated. Also can be used with only similar type of values