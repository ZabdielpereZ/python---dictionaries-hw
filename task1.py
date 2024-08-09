# 1. Real-World Python Dictionary Applications

# Objective:
# The aim of this assignment is to reinforce your understanding and application of Python dictionaries, nested collections, and dictionary methods in real-world scenarios. You will apply these concepts to solve practical problems, demonstrating your ability to manipulate and manage complex data structures.

# Task 1: Restaurant Menu Update
# You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions. This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

# Problem Statement:
# Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add a new category called "Beverages" with at least two items.
# Update the price of "Steak" to 17.99.
# Remove "Bruschetta" from "Starters".

del restaurant_menu["Starters"]["Bruschetta"]

restaurant_menu["Main Course"]["Steak"] = 17.99

# bruschetta_menu = restaurant_menu.popitem()
# print(bruschetta_menu)        # using .popitem() method didn't work

# bruschetta_menu = restaurant_menu.pop("Bruschetta", "Not Found")
# print(bruschetta_menu)        # using .pop() method didn't work

restaurant_menu['Beverages'] = {"Soda": 5.99, "Juice": 4.99}
print(restaurant_menu)
