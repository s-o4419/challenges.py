# 3. Python variable challenges

# Challenge 1 - Treasure hunter
# You find 35 gold coins. Then you find another 27.
# Create a variable for the first coins. 
# Create another variable for the new coins. 
# Calculate the total. 
# First batch of coins
first_coins = 35

# Second batch of coins
new_coins = 27

# Total coins
total_coins = first_coins + new_coins

print("Total coins:", total_coins)

# Challenge 2 - Racing car
# Your racing car travels 120 kilometers. It has already travelled 45 kilometers. 
# Calculate the remaining distance. 
total_distance = 120
distance_travelled = 45

remaining_distance = total_distance - distance_travelled
print(f"Remaining distance: {remaining_distance} km")

# Challenge 3 - Candy machine
# A candy machine stars with 50 candies. It gives away 8 candies three times. 
# Calculate how many candies remain.
# Starting number of candies
candies = 50

# Candies given away each time
give_away = 8

# Number of times candies are given away
times = 3

# Calculate remaining candies
remaining = candies - give_away * times

print("Candies remaining:", remaining)

# Challenge 4 - Football team 
# There are 11 players on each team. There are 4 teams. 
# Calculate the total number of players. 
players_per_team = 11
number_of_teams = 4

total_players = players_per_team * number_of_teams

print("Total number of players:", total_players)

# Challenge 5 - Video game
# A player starts with 100 health points. 
# Loses 20 points. 
# Gains 15 points. 
# Loses 30 points. 
# Calculate the final health. 
health = 100

for turn in range(1, 11):  # simulate 10 turns
    health -= 20           # player takes damage
    health += 15           # player recovers some health

    print(f"Turn {turn}: Health = {health}")

# Challenge 6 - Birthday Party
# Story: You are preparing a birthday party. You have 20 balloons and buy 15 more. 
# Your tasks:
# Create a variable called balloons. 
# Create another variable called new_balloons. 
# Calculate the total balloons. 
# Print the result. 
# Expected output:
# Starting balloons: 203
# New balloons: 15
# Total balloons: 35
#  Challenge 6 - Birthday Party

# Create the variables
balloons = 20
new_balloons = 15

# Calculate the total number of balloons
total_balloons = balloons + new_balloons

# Print the results
print("Starting balloons:", balloons)
print("New balloons:", new_balloons)
print("Total balloons:", total_balloons)

