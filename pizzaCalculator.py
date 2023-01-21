# fileName: pizzaCalculator.py
# Date: JAN 21 2023 @ 0:10
# Author: Bensky Sainvilus
# program description: Calculate the area and the cost for a single slice of pizza.

# input: pizza diameter, pizza price, pizza slice
DIAMETER = 2
pizzaDiameter = float(input("Enter pizza diameter (in) "))
pizzaPrice = float(input("How much is the pizza? $"))
pizzaSlice = float(input("How many slices of pizza? "))

#processing: pizza Area = DIAMETER * pizza Diameter, pizza cost = pizza Price / pizza slice 
pizzaArea = DIAMETER * pizzaDiameter
pizzacost = pizzaPrice / pizzaSlice 

# output: Area of a single slice of pizza, Cost of a single slice of pizza
print("Area of a single slice of pizza =", pizzaArea)
print("Cost of a single slice of pizza = $",pizzacost)