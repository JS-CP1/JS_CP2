# JS, 1st, Password Generator
# ----- PSUEDOCODE -----
# import random library
# create generate function
#   ask them specifying questions and define lists of each of those characters
#   repeat 4 times:
#       generate a password from the lists
#       append that password to a list of all the passwords
#   print passwords
# create main function
#   always loop
#       ask user if they want to generate passwords or leave
#       call generate function if they chose to generate passwords
#       leave if the chose leave
# ----- PSUEDOCODE & CODE -----
# import random library
import random
# create generate function
def generate():
#   ask them specifying questions and define lists of each of those characters
    length = input("How long should the password be: ")
    lowers = input("Should the password have lowercase letters (y/n): ")
    lowercases = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    uppers = input("Should the password have uppercase letters (y/n): ")
    uppercases = ["A", "B", "C", "D", "E", "F", "G","H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]
    numbers = input("Should the password have numbers letters (y/n): ")
    numberchars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    specials = input("Should the password have special characters letters (y/n): ")
    specialchars = ["!", "\\", "#", "$", "%", "&", "'", "(", ")", "*","+", ",", "-", ".", "/", ":", ";", "<", "=", ">","?", "@", "[", "\\", "]", "^", "_", "`", "{", "|","}", "~"]
#   repeat 4 times:
    for i in range(4):
#       generate a password from the lists
        pass
#       append that password to a list of all the passwords
#   print passwords

# create main function
def main():
#   always loop
    while True:
#       ask user if they want to generate passwords or leave
        option = input("What would you like to do?\n 1. Generate Passwords\n 2. Leave\n")
        while option != "1" and option != "2":
            option = input("That is not a valid option, please try a new input:\n ")
#       call generate function if they chose to generate passwords
        if option == "1":
            generate()
#       leave if the chose leave
        else:
            print("Thank you for using this program.")
            break