

# Python allows you to assign values to multiple variables in one line:

x,y,z = "orange", "banana", "Cherry"
print(x)
print(y)
print(z)


#one value to multiple varaibles 

a = b= c = "Apple";

print(a)
print(b)
print(c)


# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
#Unpacking means taking multiple values from a collection (like a list or tuple) and assigning them to multiple variables in a single line.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z) 