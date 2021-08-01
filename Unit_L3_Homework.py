# Create a list of 5 of your favourite tv shows.

Favorite_shows = []

num = 0
while num < 5:
    name = input("Enter your favourite tv show:")
    Favorite_shows.append(name)
    num += 1

# print the list its original order
print(Favorite_shows)

# Sorted the list in alphabetical order
Favorite_shows_sorted = sorted(Favorite_shows)

print(Favorite_shows_sorted)

# Print your original list
print(Favorite_shows)

# Sorted the list in reverse alphabetical order
print(sorted(Favorite_shows, reverse=True))

# Create a message indicating how many favorites TV shows you have
print("I have a total of {} tv shows.".format(len(Favorite_shows)))