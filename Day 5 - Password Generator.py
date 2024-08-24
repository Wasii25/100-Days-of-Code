#PASSWORD GENERATOR
import random
from random import shuffle
lst1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
pas = []

L = int(input("How many letters do you want in your password?\n"))
N = int(input("How many numbers do you want in your password?\n"))
S = int(input("How many symbols do you want in your password?\n"))

random.shuffle(lst1)
random.shuffle(num)
random.shuffle(sym)

for i in range(L):
    pas.append(lst1[i])
for i in range(N):
    pas.append(num[i])
for i in range(S):
    pas.append(sym[i])

p = ''.join(pas)

print(p)
