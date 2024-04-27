# To print the output
print()

'''
object - value(s) to be printed
sep (optional) - allows us to separate multiple objects inside print().
end (optional) - allows us to add add specific values like new line "\n", tab "\t"
file (optional) - where the values are printed. It's default value is sys.stdout (screen)
flush (optional) - boolean specifying if the output is flushed or buffered. Default: False
#print(object= separator= end= file= flush=)
# default seprator \n
print('Good Morning!')
print('It is rainy today')
print('Good Morning!', end= ' ')
print('It is rainy today')
# with sep parameter
print('New Year', 2023, 'See you soon!', sep= '. ')
'''
# Concatenation
print('I am ' + 'awesome.')

# Output formatting. {} act as placeholders
x = 5
y = 10
print('The value of x is {} and y is {}'.format(x,y))

## Python Input
num = input('Enter a number: ')
print('You Entered:', num)

