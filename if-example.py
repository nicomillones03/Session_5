import random

drinks = ["vodka", "tequila", "rum", "whiskey", "pisco", "mezcal", "beer", "wine"]
try:
    name = input("What is your name? ")
    age = input("How old are you? ")
    age = int(age)  # convert string to integer
    country = input("Where are you from? ")
except ValueError:
    print("Invalid age. Please enter a number.")
else:
    if age < 0 or age > 140:
        print("You are not human. This game works for humans only.")
    elif age > 120:
        print("You are too old to play the awesome drinking game.")
    elif age < 18:
        print("You are a minor. You cannot play the awesome drinking game.")
    elif (country == "USA" or country == "UAE") and age < 21:
        print("You are not allowed to drink in USA or UAE. You cannot play the awesome drinking game, please "
              "seek help.")
    else:
        print("You are an adult. You can play the awesome drinking game.")
        print("Have some", random.choice(drinks), "and enjoy the game.")
