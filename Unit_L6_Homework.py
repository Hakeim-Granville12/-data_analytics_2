# 1.	Create a simple dictionary that stores 2 variables, for example: first and last name.

Names = {'First_name': 'John', 'Last_name': 'Brown'}

# 2.	Print out those variables stored in your previous dictionary.
print(Names['First_name'])
print(Names['Last_name'])

# 3.	Add a message to those variables on printing: for example: “Hello, firstname lastname!”

Names_First_name = Names['First_name']
print("Hello! {} how are ya?".format(Names_First_name))

# #4.	Create a dictionary that holds 2 key: value pairs:
# a.	Look through your dictionary and print each pair,

Names = {
    'First_name': 'John',
    'Last_name': 'Brown',
    'Age': 25,
    'Football_Club': 'Manchester United'
}
print(Names['First_name'])
print(Names['Last_name'])
print(Names['Age'])
print(Names['Football_Club'])

# 5.	Create a nested dictionary containing three dictionaries – these dictionaries could be anything
# (favorite pets, travel locations, etc.)
# a.	Loop through the dictionaries and print a message for each.

favorite_places = {
    'summer': ['Arbua', 'Bore Bora', 'Spain'],
    'winter': ['England', 'Finland', 'Russia'],
    'spring': ['Jamaica', 'france', 'Canada']
}

for name, places in favorite_places.items():
    print(name.title() + " is the best time to visit these locations:")
    for place in places:
        print("- " + place.title())