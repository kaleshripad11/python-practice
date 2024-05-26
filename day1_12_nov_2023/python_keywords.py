import keyword as k

# Keywords are the reserved words in any of the modern programming language
# We can not use keywords in variable declaration or in function name or in class/interface names
# In python all keywords are located in the list => "kwlist" which is present in module "keyword"
# Below python code will list all the keywords in python
# Note : The keywords may vary as per the python versions.

print(k.kwlist)
print("Type of 'kwlist' =>  ",type(k.kwlist))
print("Type of 'keyword' => ",type(k))

"""
Output : 
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

Type of 'kwlist' =>  <class 'list'>
Type of 'keyword' =>  <class 'module'>
"""