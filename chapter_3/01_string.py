# String can be sliced

str_1 = "Sadaan"
str_2 = "Siddique"
# If we start to count from start, then index starts from 0 i.e 0, 1, 2, 3, 4, 5. If we count from end, then index is -1, -2, -3, -4, -5, -6

char_0 = str_1[0]
char_1 = str_1[1]

print(str_1[0]) # since string is an array of individual characters, you can print anyone form them 
    
print(str_1[0:3]) # it means print the characters which start from index 0 and end at index 2. last written (riht most is excluded i.e 3)

print()
print(str_1[-4:-1]) # we can also slice negatively. Whenever you got negative indices, write it in corresponsing positive indices.
print(str_1[2:5])
print()
print(str_1[:]) # is same as print(str_1[0:6])
print(str_1[0:6])
print()
print(str_1[:4]) # is same as print(str_1[0:4])
print(str_1[0:4])
print()
print(str_1[1:]) # is same as print(str_1[1:6])
print(str_1[1:6])
print()
print(str_1[1:6:2]) # means firstly, take characters of string from 1 to 5 then take every character after (2-1 = 1) character
print(str_2[:8:3]) # means firstly, take characters of string from 0 to 7 then take every character after (3-1 = 2) character