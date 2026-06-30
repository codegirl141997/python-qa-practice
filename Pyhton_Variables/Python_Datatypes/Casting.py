
'''
# Conversion one data type into another datatype
#For example:

Convert a string to an integer.
Convert an integer to a float.
Convert a float to a string.

Why do we need casting?

Sometimes data is in one type, but you need another type to perform an operation.

'''

age = 29;
age = int (age)
print (age+1); #output =30


# Types of casting
#1. int() ---> Convert to Integer
x= 10.9
x= int (x)
print(x)

x= "50"
print(int(x));

#2.float()--> Convert to Float

x=10;
print(float(x));

x=25;
print(float(x));


#3. Str() ==> Convert to String

x =100
y= str(x)
print(type(y))

#4. bool() ==> Convert to Boolean

print(bbol(1))
print(bool(0))
''' 
#Rule:

Non-zero numbers → True
Zero → False
Non-empty strings → True
Empty strings → False
'''