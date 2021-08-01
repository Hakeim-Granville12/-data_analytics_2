# 1.	What is Python and why is it useful?

# Python is a general purpose programming language and very useful in Data analysis and data science.


# 2.	Are the following variable names allowed in python?
# a.	1_message
# b.	Greeting_message
# c.	Message_1
# d.	First name
# e.	Full_name
# A and C are not valid variable names.


# 3.	Create a variable that holds the string “hello there!”

First_variable = "Hello There!"

print(First_variable)

# 4.	Create a variable for first name, last name and an email extension.
# Concatenating all three together to form an email address. For example: firstnamelastname@gmail.com

First_Name = "John"
Last_Name = "Brown"
Email_extension = "@gmail.com"

Email_Address = First_Name+Last_Name+Email_extension

print(Email_Address)

# 5.	Store someone you know name in a variable called name.
# Print their name in lower and uppercase using a method.

Name = "Hakeim Granville"

print(Name.lower())
print(Name.upper())

# 6.	Using a variable, ask your friend if they want to hang out on the 15th of the month.
# For example, “Do you want to hang out on the 15th of this month?”
# You should have to convert the number to a string.

day = str(12)
Question = "Do you wanna hang out on the {}th".format(day)

print(Question)
