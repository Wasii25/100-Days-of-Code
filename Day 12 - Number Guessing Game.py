from random import randint

def game():
    print('''
      / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
     / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
    / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
    \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|        
    Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.''')

    num = randint(1, 100)

    def set_difficulty():
        d = input("Choose a difficulty: Easy or hard?\n\t")

        while d.lower() not in ['easy', 'hard']:
            print("Please choose a valid difficulty")
            d = input("Choose a difficulty: Easy or hard?\n\t")

        return d


    dif = set_difficulty()

    if dif.lower() == 'easy':
        attempts = 10

    else:
        attempts = 5

    def check_guess(user_guess, actual_number):
        if user_guess > actual_number:
            print('Too high')

        elif user_guess < actual_number:
            print("Too low")

        else:
            print(f"You got it! The answer was {user_guess}")


    guess = 0
    while guess != num and attempts != 0:
        print(f"You have {attempts} attempts to guess the number")
        guess = int(input("Make a guess: "))
        check_guess(guess, num)
        attempts -= 1

        if attempts == 0:
            print(f"You've run out of guesses. The answer was {num}")
            break

game()