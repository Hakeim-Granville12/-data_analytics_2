# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(str(num) + " is an Even number.")
else:
    print(str(num) + " is an Odd number.")

if num % 4 == 0:
    print(str(num) + " is a multiple of 4.")

# 2.	Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num2 = int(input("Enter a number: "))
check = int(input("Enter another number: "))
if num2 % check == 0:
    print(str(num2) + " divides evenly by " + str(check) + ".")
else:
    print(str(num2) + " does NOT divide evenly by " + str(check) + ".")
