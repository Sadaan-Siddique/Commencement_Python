#  a list is a built-in, versatile data structure used to store a collection of multiple items in a single variable. Lists are one of the most fundamental and frequently used data types in Python programming.
# lists are Heterogeneous (can store mixed data types: int, str, float, etc.) It's a standard built-in data type in Python
# while arrays are Homogeneous (must store elements of a single, uniform data type). They requires importing a module (array or numpy)
firstList = ["Uzair",1,"Shahmeer",2,"Jacob",3 ]
# lists are mutable while strings aren't mutable means:
print(firstList[0])
firstList[0] = "Ismail"
print(firstList[0])
# Means when you apply a method on list, it'll cause change in the original list, don't create a new list.

# a list can be indexed just like a string
print(firstList[2:4])
print()
secondList = [10,3,4,8,7,6,55,89,70,0]
secondList.append(90)
secondList.sort()
print(secondList)
secondList.reverse()
print(secondList)
secondList.insert(2,2025611) # insert 2025611 in second list such that its index in the list become 2
print(secondList)
value = secondList.pop(3) # remove element at index 3
print(value)
print(secondList)
secondList.remove(10) # will remove element by its value not by its index
print(secondList)