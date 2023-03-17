# Rui Ji
# ITP 449
# HW1
# Question 5

# Write a program that prompts the user to enter their first name. It then prints whether or not their name is a palindrome.
# What is your name? Tommy
# Tommy, your name is not a palindrome!

name = input("What is your name?")
lastIndex = len(name) - 1
noPalindrome = False

for i in range(len(name)):
    if name[i] != name[lastIndex]:
        noPalindrome = True
        print(name + ", your name is not a palindrome!")
        break
    lastIndex -= 1

if not noPalindrome:
    print(name + ", your name is a palindrome!")


