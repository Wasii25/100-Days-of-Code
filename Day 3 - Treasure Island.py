#TREASURE ISLAND
print('''
 *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')
print("Welcome to Treasure Island!!")
print("Your mission is to find the treasure")

print("You are at a cross road. Where do you wanna go? Left or right? ")
D = input("Type left or right\n")
print("\n")
while D.lower() not in ['left', 'right']:
    D = input("Type left or right\n")
    print("\n")


if D.lower() == 'right':
    print("You fell into a hole!")
    print("Game over!")

else:
    print("You've come to a lake. There is an island in the middle of the lake. You can choose to swim across or to wait for a boat to arrive.")
    wait = input('Type "wait" to wait\nType "swim" to swim\n')

    while wait.lower() not in ['wait', 'swim']:
        wait = input("Type wait or swim\n")
        print("\n")

    if wait.lower() == 'swim':
        print("You get attacked by an angry trout!")
        print("Game over!")

    else:
        print("You arrive at the island unharmed. There is a house with three doors. One red, one yellow, one blue")
        door = input("Which one do you choose? Enter R, Y, B ")

        while door not in ['R', 'Y', 'B']:
            door = input("Which one do you choose? Enter R, Y, B ")

        if door == 'R':
            print("It's a room full of fire")
            print("Game over!")

        elif door == 'Y':
            print("Congratulations!! You've found the treasure chest!!\nYou have successfully completed the game!")

        else:
            print("It's a room full of wild beasts!\nGame over!!")
