while True: 
    print ('Who are you?')
    name =(input)
    if name !='Joe':
        continue
    print ('Hello, Joe. What is the password? (It is a fish.)')
    password=(input)
    if password == 'swordfish':
        break
    print ('Access granted.')
    

# IF the user enters any name besides Joe, the CONTINUE statement causes the program to jump back of the start of the loop. So the name entered MUST be Joe for the loop to go on.
# Once they make it past the first if statement they are asked for password. 
# If the password entered is 'swordfish,' then the break statement is run and the execution jumps out of the while loop to print 'Access granted.' 