# Rui Ji
# ITP 449
# HW2
# Question 3

# Write a program to ask the user to enter a password.
# Then check to see if it is a valid password based on these requirements
# a. Must be at least 8 characters long
# b. Must contain both uppercase and lowercase letters
# c. Must contain at least one number between 0-9
# d. Must contain a special character:   !, @, #, $

# If the password is not valid, ask the user to re-enter.
# This should continue until the user enters a valid password.
# After a valid password is entered, print Access Granted.
# Please enter a password. Follow these requirements Must be at least 8 characters long a. b. c. d.
# Must contain both uppercase and lowercase letters
# Must contain at least one number between 0 and 9
# Must contain a special character
# Password: HelloWorld1
# Invalid password. Try again!
# Password: Hello@World1
# Access Granted!

print("Please enter a password. Follow these requirements")
print("a. Must be at least 8 characters long")
print("b. Must contain both uppercase and lowercase letters")
print("c. Must contain at least one number between 0 9")
print("Must contain a special character !, @, #, $")

number0_9, special_symbol = False, False
need_to_retry = True
number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

while need_to_retry:
    user_input = input("Password: ")
    if len(user_input) < 8:
        print("Invalid password. Try again!")
        continue
    elif user_input == user_input.lower():
        print("Invalid password. Try again!")
        continue

    for i in range(len(user_input)):
        if user_input[i] in number_list:
            number0_9 = True
    if "!" in user_input or "@" in user_input or "#" in user_input or "$" in user_input:
        special_symbol = True
    if not (number0_9 and special_symbol):
        print("Invalid password. Try again!")
        continue
    need_to_retry = False

print("Access Granted!")



