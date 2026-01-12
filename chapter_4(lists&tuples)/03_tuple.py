# A tuple in Python is an ordered, immutable (unchangeable) collection of items, used to store multiple items in a single variable. Tuples are defined by enclosing elements in parentheses () and separating them with commas. 

# Key Characteristics

# Ordered: The items in a tuple have a defined order, which will not change.
# Immutable: Once a tuple is created, you cannot change, add, or remove its items. This immutability ensures data integrity and makes tuples more memory-efficient than lists.
# Allows Duplicates: Because they are indexed, tuples can have items with the same value.
# Heterogeneous: Tuples can contain items of different data types (strings, integers, floats, and even other tuples or lists).

# Difference between tuple and List : Lists are mutable while tuples aren't. Tuples are immutable

# Creating a tuple:
my_tuple = ("apple", "banana", "orange")
coordinates = (10, 20) # Can contain mixed data types
my_list = ["apple", "banana", "orange"]

print(type(coordinates))
print(type(my_list))

mix_tuple = (1,2,false,true,"hello",1.2)
print(type(mix_tuple))

a=() # Empty Tuple
print(type(a))
a = (1) # this initialization will make ' a ' an integer type variable whose stored value is 1
print(type(a))
a = (1,) # this initialization will make ' a ' a tuple whose stored value is 1
print(type(a))

