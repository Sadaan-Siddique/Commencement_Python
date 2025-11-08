# \n 
# \t 
# \"....\"
# \'....\'
str_1 = "My name is Muhammad Sadaan.\nI'm in \"GIKI\", enrolled in the program of \"CE\".\nPrimarily, I belong to \"Karachi\"."
str_2 = 'My name is Muhammad Sadaan.\nI\'m in \'GIKI\', enrolled in the program of \'CE\'.\nPrimarily, I belong to \'Karachi\'.'

print(str_1,"\n",str_2)
print("\\")
# By writing like this: 
# str_1 = "My name is Muhammad Sadaan.\nI'm in GIKI, enrolled in the program of CE.\nPrimarily, I belong to Karachi."
    # ^ 4 spaces here
    # print(str_1)
    # ^ 4 spaces here
# you'll get ' IndentationError: unexpected indent '
# In Python, code at the main level of a script should have zero indentation. The lines must start at the very first character position of the line.
# Why Python does this?
# Python uses indentation instead of braces ({}) or keywords to define the scope of code (like what belongs inside a function, an if statement, or a for loop). If you indent code without a block opener (like def function_name(): or if True:), Python assumes it's an error because it doesn't know what block that code is supposed to belong to.

# escape_sequences.py

# Common Escape Sequence Characters in Python

# \n - New line
print("Hello\nWorld")  
# Output:
# Hello
# World

# \t - Tab space
print("Hello\tWorld")  
# Output: Hello   World

# \\ - Backslash
print("This is a backslash: \\")  
# Output: This is a backslash: \

# \' - Single quote
print('It\'s a beautiful day!')  
# Output: It's a beautiful day!

# \" - Double quote
print("He said, \"Python is fun!\"")  
# Output: He said, "Python is fun!"

# \b - Backspace (removes one character before it)
print("Hello\bWorld")  
# Output: HellWorld

# \r - Carriage return (moves cursor to start of line)
print("Hello\rWorld")  
# Output: World  (overwrites 'Hello')

# \f - Form feed (used to move to next page in some text systems)
print("Hello\fWorld")  
# Output may look like: Hello
#                        World (depending on console)

# \a - Bell/Alert (may make a beep sound on some systems)
print("Alert\a")  
# Output: Alert (with a system beep, if supported)

# \v - Vertical tab
print("Hello\vWorld")  
# Output:
# Hello
#      World
