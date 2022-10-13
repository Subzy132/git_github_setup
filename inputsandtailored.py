# Create a little program that ask the user for the following details:
# - name
# - height
# - favourite_color
# - secrete_spirit_animal
# Then:
# Capture these inputs Print a tailored welcome message to the user
# print other details gathered, except the secret of course print the first and last letter of the secrete_spirit_animal
# * print the number of characters the secrete_spirit_animal
# hint, think about casting your data type.
def taileredmsg():
    user_name = input('Please enter your name: ')
    user_height = int(input('Please enter your height in metres: '))
    user_colour = input('What is your favourite colour: ')
    user_animal = input('Enter your secrete spirit animal: ')

    print(f'Hi {user_name}. '
          f'you are {user_height} metres tall.\n '
          f'Your favourite colour is {user_colour}.\n '
          f'Your spirit animal starts with {user_animal[0]}.\n'
          f' ends with {user_animal[-1]}.\n'
          f'it has {len(user_animal)} amount of characters :)')

    animal_guess = input("Try and guess what the spirit animal is: ")
    if animal_guess == user_animal:
        print("OMG how did you know?! :D")
    else:
        ('ah better luck next time!')

taileredmsg()