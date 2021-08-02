# 1.	Make a list of 5 or more usernames, including an admin account.  Imagine you are writing code that will welcome
# people to your application on login. Loop through the list and print your greeting.
# a.	If the admin account logs in, give them a special greeting.  They’re the admin, after all!
# b.	Other users can get the generic greeting

Username_list = ['hall24','Admin', 'Felix4','Brad23','tom10']

for user in Username_list:
    if user == "Admin":
        print("Welcome back Admin! Ready when you are")
    else:
        print("Welcome back user nice to have you!")


# 2.	Store numbers 1-10 in a list a.	Loop through the list b.	Use an if-elif-else chain inside your loop to
# print the ordinal ending for each number – for example – 1st, 2nd, 3rd … etc.

NumberedList = list(range(1, 10))
for number in NumberedList:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")

