# practicePython.org
# The exercises are separated by functions, but is not modularized. - need to be doing after learning the basics -




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
def ex02():
    print("**Even or Odd ?**")
    number = int(input("Pick a number: "));
    if(number % 2  == 0):
        print("Your number is Even !");
    else:
        print("Your number is Odd !");



"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
"""

def ex03():
    myList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    for number in myList:
        if(number < 5):
            print(number)


"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
"""

def ex04():
    myNum = int(input("Get number divisors: "))
    result = []
    listRange = list(range(1, myNum + 1))
    for number in listRange:
        if(myNum % number == 0):
            result.append(number)


    for elem in result:
        print(elem)


"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
"""

def ex05():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    result = []
    for n in a:
        if n in b:
            result.append(n)

    for elem in result:
        print(elem)


# ********************** MENU ********************
opcion = 1;
menu = "0) Exit." \
       "\n1) Guess when you're gonna turn 100 years old." \
       "\n2) Even or Odd? " \
       "\n3) Numbers less than 5 in  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] " \
       "\n4) Divisors of a number." \
       "\n5) Elems repited on other list."

while (opcion != 0):

    print(menu)
    opcion = int(input("Select an option: "))
    if opcion == 1:
        ex01()
    elif opcion == 2:
        ex02()
    elif opcion == 3:
        ex03()
    elif opcion ==4:
        ex04()
    elif opcion == 5:
        ex05()
    else:
        print("select a valid option.")