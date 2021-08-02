
# Create a list that holds 5 data variables


Name_list = ['Hakeim', 'John', 'Brad', 'Tom', 'Bob']

print(Name_list)

# Print out those variables by using a for loop.
for x in Name_list:
    print(x)


# 3.	Modify your for loop to add a message to your for loop.

for x in Name_list:
    print(x.title() + ", are names of people.")


# 4.	Use a for loop to print even numbers from 1-20.

for num in range(1, 20):
    if num % 2 == 0:
        print(num)


# 5.	Sort your list in alphabetic order.

Sorted_names = sorted(Name_list)
print(Sorted_names)


# 6.	Print out the first three elements of your list.
print(Name_list[0:3])

# 7.	Create a loop to print the last 2 elements of your list.
for name in Name_list:
    print(Name_list[0:2])
    break

