user_string = input("Enter your string : ")
reversed_user_string = ""
for i in user_string:
    reversed_user_string = i+reversed_user_string
print(reversed_user_string)

'''
Explanation : 
When control reaches to the loop, program will read each single character from 'user_string'
And then it will concatenate that single character stored in 'i' with reversed_user_string
Once all characters are traversed by 'i' in for loop condition, we will get the reverse string
'''