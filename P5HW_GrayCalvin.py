# P5HW
# Math Quiz

import random

def main():
    menu()


def menu():
    choice = 0
    while choice != 3:
        print("Welcome to the Math Quiz")
        print("")
        print("")
        print("Main Menu")
        print("-"*20)
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        print("")
        print("Please choose one of the menu options: ", end='')
        choice = int(input())


        if choice == 1:
            add()
            print("")
        elif choice == 2:
            subtract()
            print("")
        elif choice == 3:
            print("exit")
            print("The program has ended")
        else:
            print("Bad choice. Try again! ")
            print("")
    
def add():
    print("Addition Function")

def subtract():
    print("Subtraction Function")



main()
