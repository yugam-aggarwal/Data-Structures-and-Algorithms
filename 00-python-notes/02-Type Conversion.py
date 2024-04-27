#Type Conversion

#Implicit Type Conversion
#Implicit conversion is performed by the Python interpreter without the programmer’s intervention.
#Python automatically converts one data type to another data type. This process doesn't need any user involvement.
#For example:
#Converting int to float, float to complex, etc.
#Example:
#Converting integer to float
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

#Converting float to complex
num_flo = 1.23
num_complex = 1.23 + 5j

num_new = num_flo + num_complex

print("datatype of num_flo:",type(num_flo))
print("datatype of num_complex:",type(num_complex))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

#Explicit Type Conversion
#In Explicit Type Conversion, users convert the data type of an object to required data type. We use the predefined functions like int(), float(), str(), etc to perform explicit type conversion.
#This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.
#Syntax:
#<required_datatype>(expression)
#Typecasting can be done by assigning the required data type function to the expression.
#Example:
#Converting string to integer
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))

#Converting string to float
num_str = "15.5"
num_str = float(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

#Converting integer to string
num_int = 123
num_str = str(num_int)
print("Data type of num_str after Type Casting:",type(num_str))

#Converting string to list
#Splitting the string and converting it to list
num_str = "12345"
num_list = list(num_str)
print("Data type of num_list:",type(num_list))
print(num_list)

#Converting list to string
#list of strings
num_list = ['1', '2', '3', '4', '5']
num_str = ''.join(num_list)
print("Data type of num_str:",type(num_str))
print(num_str)

#Converting tuple to set
#tuple
num_tup = ('1', '2', '3', '4', '5')
num_set = set(num_tup)
print("Data type of num_set:",type(num_set))
print(num_set)

#Converting set to list
#set
num_set = {'1', '2', '3', '4', '5'}
num_list = list(num_set)
print("Data type of num_list:",type(num_list))
print(num_list)

#Converting list to tuple
#list
num_list = ['1', '2', '3', '4', '5']
num_tup = tuple(num_list)
print("Data type of num_tup:",type(num_tup))
print(num_tup)

#Converting integer to binary, octal and hexadecimal
num = 100

print("The decimal value of", num, "is:")
print(bin(num), "in binary.")
print(oct(num), "in octal.")
print(hex(num), "in hexadecimal.")

#Converting binary, octal and hexadecimal to integer
#binary
num = '0b1100100'
print("The decimal value of", num, "is:", int(num, 2))

#octal
num = '0o144'
print("The decimal value of", num, "is:", int(num, 8))

#hexadecimal
num = '0x64'
print("The decimal value of", num, "is:", int(num, 16))

#Converting integer to float
#integer
num_int = 100
print("Data type of num_int:",type(num_int))

num_flo = float(num_int)
print("Data type of num_flo:",type(num_flo))

#Converting float to integer
#float
num_flo = 100.123
print("Data type of num_flo:",type(num_flo))

num_int = int(num_flo)
print("Data type of num_int:",type(num_int))

#Converting float to complex
#float
num_flo = 1.23
print("Data type of num_flo:",type(num_flo))

num_com = complex(num_flo)
print("Data type of num_com:",type(num_com))

#Converting complex to float
#complex
num_com = 1.23 + 5j
print("Data type of num_com:",type(num_com))

num_flo = float(num_com)
print("Data type of num_flo:",type(num_flo))

#Converting string to complex
#string
num_str = "1.23"
print("Data type of num_str:",type(num_str))

num_com = complex(num_str)
print("Data type of num_com:",type(num_com))

#Converting complex to string
#complex
num_com = 1.23 + 5j
print("Data type of num_com:",type(num_com))

num_str = str(num_com)
print("Data type of num_str:",type(num_str))

    
