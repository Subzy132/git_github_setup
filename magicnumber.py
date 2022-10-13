import random
## User story 1 ## As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

# We should define/assign number to a variable called magic_number --> might be cool to use the py library random

magic_number= random.randint(0, 9)

# I need to ask user for input

user_guess = int(input('Please guess a number from 1-10: '))


# I need to check if this input matches a magic_number

if user_guess == magic_number:
    print("You have guessed correctly! Well done!")
else:
    print("You have guessed incorrectly, the random number was: " + str(magic_number))


# I need to let the user know if the response was correct or not
#self five