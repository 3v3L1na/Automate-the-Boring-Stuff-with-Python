name= ''
while not name: 
    print ('Enter your name:')
    name (input)
print ('How many guests will you have?')
numOfGuests=int (input())
if numOfGuests:
    print ('Be sure to have enough room for all your guests.')
    print ('Done')
    
# If the user enters a blank string for a name as shown above, (while there is no name) then the while statement will be true.
# And the program continues to ask for the name. ('Enter your name')
# If the value for the numOfguests is not 0, then the condition is considered to be True and the program will print a reminder for a user. 
# If we used != instead of = in the name and numOfGuests variables, our code would have been easier to read. 

while True:
    print ('Who are you?')
    name (input)
    if name !='Joe':
        print ('Hello, Joe. What is the password? (It is a fish.)')
        password= (input)
        if password =='swordfish':
            print ('Access granted.')
        else: 
            print ('Enter password:')

# While the condition is true, the program will keep printing 'Who are you?'
# As soon as the name 'Joe' is inputted, the program salutes the person and asks for the password. 
# In the next stage of the program, the person tries for the password and if a password is correctly typed, then, the words 'Access granted' are printed. 