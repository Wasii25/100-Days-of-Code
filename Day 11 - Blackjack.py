#BLACKJACK
import random

card_deck_values = {
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
}


card_deck = [key for key in card_deck_values]

def deal_cards(deck):

    random.shuffle(card_deck)
    a = card_deck.pop(0)
    deck.append(a)


def calc_score(deck):
    score = 0
    for i in deck:
        score += card_deck_values[i]

    return score


def check_for_ace(deck):
    if 'A' in deck:
        if calc_score(deck) <= 21:
            card_deck_values['A'] = 11
        else:
            card_deck_values['A'] = 1


def hit(pl):
    a = card_deck.pop(0)
    pl.append(a)
    check_for_ace(pl)

def stand(dealer_score, player_score, dealer_deck):

    while dealer_score <= player_score and dealer_score <= 21:
        dealer_deck.append(card_deck[0])
        check_for_ace(dealer_deck)

def black_jack(deck):
    if 'A' in deck and 'K' in deck:
        return True
    elif 'A' in deck and 'Q' in deck:
        return True
    elif 'A' in deck and 'J' in deck:
        return True
    else:
        return False


def win(player_deck, dealer_deck, pscore, dscore):
    if black_jack(player_deck):
        print("Player wins by Blackjack!!")
        print(f'{player_deck}')
        print(f'{dealer_deck}')

    elif black_jack(dealer_deck):
        print("Dealer wins by Blackjack!!")
        print(f'{player_deck}')
        print(f'{dealer_deck}')

    elif (pscore <= 21) and (pscore > dscore):
        print("Player wins! win function")
        print(f'{player_deck}')
        print(f'{dealer_deck}')

    elif (pscore < dscore) and (dscore <= 21):
        print("Dealer wins")
        print(f'{player_deck}')
        print(f'{dealer_deck}')

    else:
        print("It's a draw. PUSH!!")
        print(f'{player_deck}')
        print(f'{dealer_deck}')


def game():
    pl = input("Do you want to play a game of BlackJack?? Type 'y' to play 'n' to exit\n\t")

    while pl.lower() not in ['y', 'n']:
        print("Please enter a valid option")
        pl = input("Do you want to play a game of BlackJack?? Type 'y' to play 'n' to exit\n\t")

    if pl.lower() == 'y':
        game_on = True

    else:
        game_on = False

    while game_on:
        print('\n'*100)
        print('''
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        '-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
              |  \/ K|                            _/ |                
              '------'                           |__/      ''')
        players_deck = []
        dealers_deck = []

        #DEALING CARDS AND CALCULATING SCORE
        deal_cards(players_deck)
        deal_cards(players_deck)

        deal_cards(dealers_deck)

        player_score = calc_score(players_deck)
        dealer_score = calc_score(dealers_deck)

        #DISPLAYING CARDS AND SCORE

        print(f"Your cards: {players_deck}     Your score = {player_score}")
        print(f"Dealer's cards: {dealers_deck}")
        if black_jack(players_deck):
            print("Player wins")
            print(f'{players_deck}')
            break

        #HIT OR STAND
        h_or_s = input("Does the player choose to hit or stand? Type 'h' to hit and 's' to stand\n\t")

        while h_or_s not in ['h', 's']:
            print("Please enter a valid option!")
            h_or_s = input("Does the player choose to hit or stand? Type 'h' to hit and 's' to stand\n\t")

        while h_or_s == 'h':
            hit(players_deck)
            if calc_score(players_deck) > 21:
                print("Player loses")
                game_on = False
                break
            else:
                check_for_ace(players_deck)
                player_score = calc_score(players_deck)
                print(f"Your cards: {players_deck}     Your score = {player_score}")
                print(f"Dealer's cards: {dealers_deck}")
                h_or_s = input("Does the player choose to hit or stand? Type 'h' to hit and 's' to stand\n\t")

        if h_or_s == 's':
            check_for_ace(dealers_deck)
            stand(dealer_score, player_score, dealers_deck)
            if calc_score(dealers_deck) > 21:
                print("Dealer loses")
                game_on = False
                break
            else:
                dealer_score = calc_score(dealers_deck)

        win(players_deck, dealers_deck, player_score, dealer_score)

        i = input("Do you want to play a new game? Type 'y' or 'n' \n\t")
        while i not in ['y', 'n']:
            print("Please enter a valid option!")
            i = input("Do you want to play a new game? Type 'y' or 'n' \n\t")

        if i.lower() == 'y':
            game()


game()
