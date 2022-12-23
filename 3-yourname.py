spam = 0                           # This is an example of a loop where, as long spam is under 5, the sentence 'Ahoy mundo' will keep being printed. 
while spam <5:
    print('Ahoy, mundo')
    spam=spam +1                   # The integer in spam is incremented by one at the end of each loop iteration. Loop executes 5 times before spam < 5 is False. 

             



name=''                          
while name != 'your name':
    print ('Please type your name.')
    name (input)
print ('Thank you!')

 # The program sets the name variable to an empty string. (This is so that the second condition will evaluate to True, so the while clause starts.)
 # The code inside this clause asks the user to type their name, which is assigned to the name variable.
 # If the value in the name is not equal to 'your name', the condition is True and the execution enters a while clause again. 
 # But once the user types 'your name' the while clause will be False. 
 # The program skips the 'Please type your name' part and goes to execute the print ('Thank you!) part, thus ending the while loop. 
 # If you never enter 'your name' the while loop condition will never be False and the program will just keep asking forever. 
 
while True: 
     print ('Please type your name.')
     name (input)
     if name == 'your name':
        break
print ('Thank you!')

# The first line creates an infinite loop - a While loop whose condition is always true. The program can exit it only when a Break statement is executed. 
# The program asks the user to type 'your name.' But then an if statement gets executed to make sure that the break statement is run and 'Thank you' printed. 