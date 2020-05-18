# practicePython.org
# The exercises are separated by functions, but is not modularized. - need to be doing after learning the basics -
import os



"""
1)Create a program that asks the user to enter their name and their age.
  Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""

def ex01():

    print("** Guess when you're gonna turn 100 years old. ** ")
    name = input("What is your name ? : ")
    yearOfBirth = int(input("Year of birth: "))

    result = yearOfBirth + 100;

    print(name + " you are going to turn 100 years old on", result)



"""
2) Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
"""




# ********************** MENU ********************
opcion = 1;
menu = "0) Exit." \
       "\n1) Guess when you're gonna turn 100 years old."

while (opcion != 0):

    print(menu)
    opcion = int(input("Select an option: "))
    if opcion == 1:
        ex01()
    else:
        print("select a valid option.")