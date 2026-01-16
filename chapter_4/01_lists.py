#  a list is a built-in, versatile data structure used to store a collection of multiple items in a single variable. Lists are one of the most fundamental and frequently used data types in Python programming.
# lists are Heterogeneous (can store mixed data types: int, str, float, etc.) It's a standard built-in data type in Python
# while arrays are Homogeneous (must store elements of a single, uniform data type). They requires importing a module (array or numpy)
firstList = ["Uzair",1,"Shahmeer",2,"Jacob",3 ]
# lists are mutable while strings aren't mutable means:
print(firstList[0])
firstList[0] = "Ismail"
print(firstList[0])
# a list can be indexed just like a string
print(firstList[2:4])   