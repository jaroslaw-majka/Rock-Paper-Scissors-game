import random


# First the program will take users input on his RPS choice
def user_choice():
    print('-' * 30)
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')
    chosen_value = int(input('Please choose one by entering a number corresponding to your choice: '))


# Then it will generate random computers choice
# Then it will compare both and choose a winner!


if __name__ == '__main__':
    user_choice()
