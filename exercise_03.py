#Exercise 03
#Take in an integer greater than 1. Print out the cubes of each integer from 0 to the inputted integer.

print('Enter an integer greater than 1: ', end= " ")
userInput = int(input())
if userInput > 1:
    for item in range(1,userInput + 1):
        print('The cube of ',str(item), ' is ', item * item * item)
else:
    print('you failed to enter in a proper integer')