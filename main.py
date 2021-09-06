import random


# First the program will take users input on his RPS choice
def user_choice():
    print('-' * 30)
    print('1. Rock')
    print('2. Paper')
    print('3. Scissors')
    print('4. Close the game')
    chosen_value = int(input('Please choose one by entering a number corresponding to your choice: '))
    return chosen_value


# Then it will generate random computers choice
def computers_choice():
    return random.choice(range(1, 4))


def decision_formatter(num):
    if num == 1:
        return "Rock"
    elif num == 2:
        return "Paper"
    elif num == 3:
        return "Scissors"
    elif num == 4:
        return quit()


# Then it will compare both and choose a winner!
def winner_decider():
    user_score, computer_score = 0, 0
    while True:
        user_chose = decision_formatter(user_choice())
        computer_chose = decision_formatter(computers_choice())
        print(f'User {user_chose} and Computer {computer_chose}')

        # Rock crushes scissors
        if user_chose == "Rock" and computer_chose == "Scissors":
            print('Your rock crushes computers scissors! Congratulations!')
            user_score += 1
        elif user_chose == "Scissors" and computer_chose == "Rock":
            print("Computers rock crushed your scissors! So sorry (not)!")
            computer_score += 1
        # Scissors cut paper
        elif user_chose == "Scissors" and computer_chose == "Paper":
            print('Your scissors cut computers paper! You won!')
            user_score += 1
        elif user_chose == "Paper" and computer_chose == "Scissors":
            print('Computers scissors cut your paper. You loose!')
            computer_score += 1
        # Paper covers rock
        elif user_chose == "Paper" and computer_chose == "Rock":
            print('Your paper covers computers rock, you win!')
            user_score += 1
        elif user_chose == "Rock" and computer_chose == "Paper":
            print('Computers paper covers your rock. You loose, again.')
            computer_score += 1
        # Tie!
        else:
            print('It\'s a tie!')
        print(f'Your score {user_score}\nComputer\'s score {computer_score}')


if __name__ == '__main__':
    winner_decider()
