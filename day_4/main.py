# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# love_score = random.randint(1, 100)
# print(f"Your love score is {love_score}")


# import random

# headsortails = random.randint(0, 1)
# if headsortails == 1:
#   print("Heads")
# else:
#   print("Tails")

# states_of_america = [
#     "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", 
#     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", 
#     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", 
#     "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", 
#     "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", 
#     "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", 
#     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", 
#     "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", 
#     "Montana", "Washington", "Idaho", "Wyoming", "Utah", 
#     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"
# ]

# print(states_of_america[0])

# names = names_string.split(", ")
# # names_string contains the input values provided. 
# # The code above converts the input into an array seperating
# # each name in the input by a comma and space.
# # 🚨 Don't change the code above 👆
# import random

# randomchoice = random.choice(names)
# print(f"{randomchoice} is going to buy the meal today!")

# names = names_string.split(", ")

# import random

# # Get the total number of items in list.
# num_items = len(names)
# # Generate random numbers between 0 and the last index. 
# random_choice = random.randint(0, num_items - 1)
# # Choose and print a random name.
# print(names[random_choice])

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])

#TREASURE MAP

# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?

# letter = position[0].lower()
# abc = ["a", "b", "c"]
# letter_index = abc.index(letter)
# number_index = int(position[1]) -1
# map[number_index][letter_index] = "X"


# print(f"{line1}\n{line2}\n{line3}")