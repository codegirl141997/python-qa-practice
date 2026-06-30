# String
x = "Hello"
print(x)
print(type(x));

# Integer
x = 10
print(x)
print(type(x));

# Float
x = 10.25
print(x)
print(type(x));

# Complex
x = 3 + 4j
print(x)
print(type(x));

# List
x = ["apple", "banana", "Cherry"]
print(x)
print(type(x));

# Tuple
x = ("radha", "jay", "krishna")
print(x)
print(type(x));

# Range
x = range(6)
print(list(x))
print(type(x));
# Dictionary
x = {"name": "Dhanashri", "age": 36}
print(x)

# Set
x = {"apple", "banana", "cherry"}
print(x)
print(type(x));

# Frozen Set
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x));
# Boolean
x = True
print(x)

# Bytes
x = b"hello"
print(x)

# Bytearray
x = bytearray(5)
print(x)

# Memoryview
x = memoryview(bytes(5))
print(x)



#Datatypes in the Python and how to get type at  run time 

Str = "Hello world"
print (Str)

b,c,d=5,6.4,"Great"

# If there is 2 datatypes you concat it then we use formast method

#print ("Value is"+b)

print ("{} {}".format("Value is",b))

print (type(b)) # it wil tell what  type varibale it is

print(type(c))

print(type(d))


''' 

Python DataType - Numeric : int, long, float , complex 
Pyhton DataType - String (+ operator supports for the 2 strings )
Python DataType - list
Python DataType - tuple
Dictionary 

we dont need to mention the datatype 
'''



values = [1,2,"Dhanu",4,5] # List contains any values and can be differnt data types

print (values[0]) #1

print(values[3])#4

print(values[-1]) #-1 means it ll print the last value  = 5 

print(values[1:3]) # 2,Dhanu,4

values.insert(3,"Radha")

print(values)

values.append("End")

print(values)


values [2] ="Jay"  # Updating the value of 2nd index

del values[0]

print(values)


''' List → Mutable (you can change it after creation)
Tuple → Immutable (you cannot change it once created)

List uses square brackets []
Tuple uses parentheses ()

error when update data in the tuple : tuple' object does not support item assignment

''' 


val = (1,2,"Rahul",4.5)
print(val)

#val[2]= "shri"

dic = {"a":2,4:"abcd","c":"Hello World"}

print (dic)

print(dic[2])

print("hello")
