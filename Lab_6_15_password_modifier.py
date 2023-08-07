'''Question:

Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending "!" to the end of the input string.

i becomes 1
a becomes @
m becomes M
B becomes 8
s becomes $
Ex: If the input is:

mypassword
the output is:

Myp@$$word!'''

#My solution

#input: get the current password
current_password = input()
#assign a blank string variable to hold the new concatenated password
better_password = ''
#use the str.replace(old value, new value) method to make the needed swaps
''' Type your code here. '''
current_password = current_password.replace("i", "1")
current_password = current_password.replace("a", "@")
current_password = current_password.replace("m", "M")
current_password = current_password.replace("B", "8")
current_password = current_password.replace("s", "$")
#add the new current password to the "!" ending to make the better password
better_password = current_password + "!"
#ouput better password
print(better_password)



