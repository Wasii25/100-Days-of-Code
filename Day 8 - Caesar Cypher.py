#CAESAR CYPHER

print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88
''')
lst1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lst2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encode(original_text, shift_number1):
    cypher_text = ''

    for letter in original_text:
        if letter in lst1:
            shifted_position = lst1.index(letter) + shift_number1

            shifted_position %= len(lst1)
            cypher_text += lst1[shifted_position]

        elif letter in lst2:
            shifted_position = lst2.index(letter) + shift_number1

            shifted_position %= len(lst2)
            cypher_text += lst2[shifted_position]

        else:
            cypher_text += letter
    print(cypher_text)


def decode(encrypted_text, shift_number2):
    original_text = ''

    for letter in encrypted_text:
        if letter in lst1:
            shifted_position = lst1.index(letter) - shift_number2

            shifted_position %= len(lst1)
            original_text += lst1[shifted_position]

        elif letter in lst2:
            shifted_position = lst2.index(letter) - shift_number2

            shifted_position %= len(lst2)
            original_text += lst2[shifted_position]

        else:
            original_text += letter

    print(original_text)

game_on = True

while game_on:

    user_choice = input("Type 'encode' to encrypt and 'decode' to decrypt\n\t")
    message = input("Enter the message:\n\t")
    shift_number = int(input("Enter the shift number: "))

    if user_choice.lower() == 'encode':
        encode(message, shift_number)

    else:
        decode(message, shift_number)

    w = input("Do you want to go again? Y or N\n\t")

    if w.lower() == 'y':
        game_on = True
    else:
        game_on = False
