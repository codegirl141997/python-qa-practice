'''
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:

'''
print (" Its's fine")
print(" he is called it ")
print('he is called john')

# Assign String to a Variable
a = "hello"
print(a)

# Multiline Strings

a= """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua
"""

print(a)


#String Index
text= "Python"
''' 
Character           P Y T H O N 
Index               0 1 2 3 4 5
Neagtive Index      -6 -5 -4 -3 -2 -1
'''

print(text[0])
print(text[5])
print(text[-1])


# Python - Slicing Strings

# You can return a range charcter by uisng the slice the syntax 
#Get the characters from position 2 to position 5 (not included):
b= "Hello world!" #  space will consider as index 
print(b[2:5])
print(b[1:6]) 

#Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print(b[2:]) # llo, World!


#Modify Strings:
#1. The upper() method returns the string in upper case:
a = "Hello World";
print(a.upper());

#2. The lower() method returns the string in lower case:

a = "PYTHON LEARNING";
print(a.lower());

#3. Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

a = "  hello   World   "
print(a.strip())


#4.Replace String

a = "Hello World"
print(a.replace("o","k"))

#5.Split String
#The split() method returns a list where the text between the specified separator becomes the list items.

a = "Hello, World!"
print(a.split(",")) 
print(a.split("o")) 

# ==========================================================================================================================================

#Concat String:

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# ==========================================================================================================================================

#sTRING fORMAT

age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)

age = 36
