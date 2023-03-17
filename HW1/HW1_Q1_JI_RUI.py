# Rui Ji
# ITP 449
# HW1
# Question 1

# Write a program that prompts the user to enter a password then prints the length of the password.
# Enter your password: hello
# Your password is 5 character long.

userPassword = input("Enter your password:")
length = len(userPassword)
print("Your password is " + str(length) + " character long")
