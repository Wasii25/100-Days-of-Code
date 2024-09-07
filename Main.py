import art
import game_data
import random

def win(a_f, b_f, user_inp):
    if user_inp.lower() == 'a':
        if a_f > b_f:
            return True
        else:
            return False
    else:
        if a_f < b_f:
            return True
        else:
            return False


def pic():
    i = random.randint(0, len(game_data.data)-1)

    return game_data.data[i]['name'] + ', ' + game_data.data[i]['description'] + ', from ' + game_data.data[i]['country'], game_data.data[i]['follower count']


game_on = True
win_counter = 0

B, b_followers = pic()

while game_on:
    print(art.logo)
    A = B
    a_followers = b_followers
    B, b_followers = pic()

    if A == B:
        B, b_followers = pic()

    print(f"Compare A: {A}")

    print(art.vs)

    print(f'compare B: {B}')
    user_input = input("Who has more followers; A or B? ")

    while user_input.lower() not in ['a', 'b']:
        print("Enter a valid input")
        user_input = input("Who has more followers; A or B? ")

    w = win(a_followers, b_followers, user_input)

    if w:
        win_counter
        win_counter += 1
        print("\n"*100)
        print(f"You are right! Current score {win_counter}")

    else:
        print("Sorry, that's wrong. You lose")
        print(f"Your score was {win_counter}")
        game_on = False



