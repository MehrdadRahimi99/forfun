import random   # Importing the "random" module to generate random numbers.

roll_count = int(input("How many dice do you want to roll? "))   # Asking the user for the number of dice rolls they want.

for i in range(roll_count):   # Looping from 0 up to the number of rolls specified by the user.
    dice_roll = random.randint(1, 6)   # Generating a random integer between 1 and 6 (inclusive) and storing it in the variable 'dice_roll'.
    print(dice_roll)   # Displaying the value of 'dice_roll' on the console. This will be repeated as many times as the loop runs. 
