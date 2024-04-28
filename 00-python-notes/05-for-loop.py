#To iterate over sequences such as lists, strings, tuples

languages = ['Swift', 'Python', 'Go']
# access elements of the list one by one
for i in languages:
    print(i)

language = 'Python'
# iterate over each character in language
for x in language:
    print(x)

#for Loop with Python range()
#the range() function returns a sequence of numbers.
values = range(4)
#Here, range(4) returns a sequence of 0, 1, 2 ,and 3.

# iterate from i = 0 to i = 3
for i in range(4):
    print(i)

#for loop with else clause
digits = [0, 1, 5]
for i in digits:
    print(i)
else:
    print("No items left.")

#we didn't use any of the elements of the list.In such cases, it is clearer to use the _ (underscore) as the loop variable. The _ indicates that a loop variable is a placeholder and its value is intentionally being ignored.
languages = ['Swift', 'Python', 'Go']
# using _ for placeholder variable
for _ in languages:
    print('Hi')

# outer loop 
for i in range(2):
    # inner loop
    for j in range(2): 
        print(f"i = {i}, j = {j}")

