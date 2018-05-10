"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
   Hint: how does an even / odd number react differently when divided by 2?
   Extras:
         If the number is a multiple of 4, print out a different message.
         Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
         If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

num = int(input("Enter a number: "))
if num % 2:
        print("Number is odd")
else:
    print("Number is even")
    if num % 4:
        print("Number is not a multiple of 4")
    else:
        print("Number is a multiple of 4")

num, check = input("\nEnter any 2 numbers separated by commas: ").split(",")
if int(num) % int(check):
    print("%s does not divide %s evenly" % (check, num))
else:
    print("%s divides %s evenly" % (check, num))
