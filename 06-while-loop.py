'''
while Loop Syntax

while condition:
    # body of while loop

Here,
The while loop evaluates the condition.
If the condition is true, body of while loop is executed. The condition is evaluated again.
This process continues until the condition is False.
Once the condition evaluates to False, the loop terminates.

We can use a break statement inside a while loop to terminate the loop immediately without checking the test condition. 
while True:
    user_input = input('Enter your name: ')

    # terminate the loop when user enters end
    if user_input == 'end':
        print(f'The loop is ended')
        break  

    print(f'Hi {user_input}')

while loop with an else clause
counter = 0

while counter  <  2:
    print('This is inside loop')
    counter = counter + 1
else:
    print('This is inside else block')

'''
