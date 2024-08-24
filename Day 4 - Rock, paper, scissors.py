#ROCK, PAPER, SCISSORS
import random
player_input = int(input("What do you choose?\nEnter 0 for rock\nEnter 1 for paper\nEnter 2 for scissors\n"))
system_input = random.randint(0,3)

while player_input not in [0,1,2]:
    print("Please enter a valid option")
    player_input = input("What do you choose?\nEnter 0 for rock\nEnter 1 for paper\nEnter 2 for scissors\n")


def display(i):
    if i == 0:
        print(''''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
    elif i == 1:
        print(''''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
    else:
        print(''''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')

display(player_input)
display(system_input)

def com(p, s):
    if p == 0:
        if s == 0:
            print("It's a draw")
        elif s == 1:
            print("System wins")
        else:
            print("Player wins")
    elif p == 1:
        if s == 0:
            print("Player wins")
        elif s == 1:
            print("It's a draw")
        else:
            print("System wins")
    else:
        if s == 0:
            print("System wins")
        elif s == 1:
            print("Player wins")
        else:
            print("It's a draw")

com(player_input,system_input)