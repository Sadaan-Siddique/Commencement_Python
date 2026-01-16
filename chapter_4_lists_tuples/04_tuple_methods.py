# ================== TUPLE METHODS & OPERATIONS ==================

# Creating a tuple
t = (1, 2, 3, 2, 4, 2)

# 1. count() → Counts how many times a value appears in the tuple
print("Count of 2:", t.count(2))   # Output: 3

# 2. index() → Returns index of first occurrence of a value
# If the value is not present, Python raises an error.
print("Index of 3:", t.index(3))   # Output: 2

# 3. len() → Returns total number of elements in the tuple
print("Length of tuple:", len(t))  # Output: 6

# 4. Indexing → Access elements using index number
print("First element:", t[0])      # Output: 1
print("Last element:", t[-1])      # Output: 2

# 5. Slicing → Access a range of elements
print("Sliced tuple (1:4):", t[1:4])  # Output: (2, 3, 2)

# 6. Membership operator (in) → Checks if value exists in tuple
print("Is 4 in tuple?", 4 in t)    # Output: True

# 7. Tuple concatenation (+) → Joins two tuples
t2 = (5, 6)
print("Concatenated tuple:", t + t2)  # Output: (1, 2, 3, 2, 4, 2, 5, 6)

# 8. Tuple repetition (*) → Repeats tuple elements
print("Repeated tuple:", t2 * 3)   # Output: (5, 6, 5, 6, 5, 6)

# Unpacking: Tuples can be unpacked into individual variables
a, b, c = t
print(a, b, c)

# NOTE:
# Tuples are IMMUTABLE → elements cannot be changed, added, or removed
# Example (this will cause an error):
# t[0] = 10   ❌ Not allowed


