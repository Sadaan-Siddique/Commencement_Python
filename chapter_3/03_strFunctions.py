
# string_functions.py

# Most Commonly Used String Functions in Python

# Define a sample string for demonstration
name = "Sadaan Siddique"
depart_1 = "computer enginnering"
depart_2 = " computer science"
text = "  Hello, World!  "

# 1. upper() - Converts all characters to uppercase
print(text.upper())  # Output: "  HELLO, WORLD!  "

# 2. lower() - Converts all characters to lowercase
print(text.lower())  # Output: "  hello, world!  "

# 3. strip() - Removes leading and trailing whitespace
print(text.strip())  # Output: "Hello, World!"

# 4. lstrip() - Removes leading (left-side) whitespace
print(text.lstrip())  # Output: "Hello, World!  "

# 5. rstrip() - Removes trailing (right-side) whitespace
print(text.rstrip())  # Output: "  Hello, World!"

# 6. replace(old, new) - Replaces all occurrences of a substring with another
print(text.replace("World", "Python"))  # Output: "  Hello, Python!  "

# 7. split() - Splits string into a list (by default using space)
print(text.split())  # Output: ['Hello,', 'World!']

# 8. join() - Joins elements of an iterable (like list) into a single string
words = ['Hello', 'Python', 'World']
print(" ".join(words))  # Output: "Hello Python World"

# 9. find() - Returns the index of the first occurrence of a substring (-1 if not found)
print(text.find("World"))  # Output: 9

# 10. index() - Similar to find(), but raises an error if not found
print(text.index("World"))  # Output: 9

# 11. count() - Returns the number of occurrences of a substring
print(text.count("l"))  # Output: 3

# 12. startswith() - Checks if string starts with a given substring
print(text.startswith("  He"))  # Output: True

# 13. endswith() - Checks if string ends with a given substring
print(text.endswith("!  "))  # Output: True

# 14. capitalize() - Capitalizes the first letter and makes others lowercase
print("python".capitalize())  # Output: "Python"

# 15. title() - Capitalizes the first letter of each word
print("hello world".title())  # Output: "Hello World"

# 16. swapcase() - Swaps uppercase to lowercase and vice versa
print("Hello".swapcase())  # Output: "hELLO"

# 17. isalpha() - Checks if all characters are alphabetic
print("Hello".isalpha())  # Output: True

# 18. isdigit() - Checks if all characters are digits
print("123".isdigit())  # Output: True

# 19. isalnum() - Checks if all characters are alphanumeric
print("Hello123".isalnum())  # Output: True

# 20. isnumeric() - Checks if all characters are numeric
print("123".isnumeric())  # Output: True

# 21. isspace() - Checks if all characters are whitespace
print("   ".isspace())  # Output: True

# 22. center(width, char) - Centers string with given width and fill character
print("Hi".center(10, '-'))  # Output: "----Hi----"

# 23. zfill(width) - Pads string on the left with zeros
print("42".zfill(5))  # Output: "00042"

# 24. encode() - Encodes the string into bytes
print("Hello".encode())  # Output: b'Hello'

# 25. format() - Formats string with placeholders
print("My name is {} and I am {} years old.".format("Sadaan", 20))
# Output: "My name is Sadaan and I am 20 years old."


print(len(name)) # it tells the length of the string
print()
print(name.endswith("ue")) # it checks whether the string ends with the given characters in quotation marks or not. It returns either true or false.
print(name.endswith("ue ")) # it also counts space as a character
print()
print(name.startswith("Sa")) # it checks whether the string starts with the given characters in quotation marks or not. It returns either true or false.
print(name.startswith("sa")) # Capitalcase alphabet and smallcase alphabet are different characters. So, it will return false.
print()
print(depart_1.capitalize()) # It will capitalize the first charater of string.
print(depart_2.capitalize()) # it considers space as a first character if it's at the 0 indedx of string( basically is an array of characters ) and will not capitalize the character at index 1.