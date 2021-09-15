# fileHandling.py
# Victor Sullivan
# 20210914
# Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file.

import os

prepPy = open("pies.txt", "w")
prepPy.write("Crust,Filling,Temp")
prepPy.close()

intoTheOven = open("pies.txt", "r")
print("Baking Py's:")
print()
print(intoTheOven.read())
intoTheOven.close()

myPyRecipes = open("pies.txt", "a")
myPyRecipes.write("\n")
myPyRecipes.write("Fluffy, Cherry, 450 \n")
myPyRecipes.write("Sweet, Pecan, 425 \n")
myPyRecipes.write("Grahm Cracker, Cheese, No Bake \n")
myPyRecipes.close()

pathToPy = ("pies.txt")



os.remove(pathToPy)
