"""Create a program that asks the user to enter their name and their age.
   Print out a message addressed to them that tells them the year that they will turn 100 years old.
   Extras:
         Add on to the previous program by asking the user for another number and printing out that many copies
         of the previous message. (Hint: order of operations exists in Python)
         Print out that many copies of the previous message on separate lines.
         (Hint: the string "\n is the same as pressing the ENTER button)"""
import datetime

copies = int(input("Enter the number of times the message should be displayed: "))
for i in range(0, copies):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    yearsTo100 = 100 - age
    year100 = int(datetime.date.today().year) + yearsTo100
    print("Hey %s, you will  be 100 years old in %d\n" % (name, year100))
