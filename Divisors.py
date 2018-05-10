"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)"""

num = int(input("Enter the number you wish to check: "))
divisor = []

divisor = [i for i in range(1, int((num/2)+1)) if num % i is 0]

print("The divisors of", num,  "are: ", divisor)

