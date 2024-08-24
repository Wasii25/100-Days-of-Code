#PYHTON PIZZA
print("Welcome to Python Pizza!")
print("Small Pizza(S): $15")
print("Medium Pizza(S): $20")
print("Large Pizza(S): $25")
print("\n")
print("Extra Toppings:\nMushrooms on small size pizza: +$2\nMushrooms on medium and large size pizzas: +$3\nAdd cheese for any size pizza: +$1")

size = input("Enter the size - S, M or L? ")

while size not in ['S', 's', 'M', 'm', 'L', 'l']:
    size = input("Enter the size - S, M or L? ")

if size == 'S' or size == 's':
    total = 15
elif size == 'M' or size == 'm':
    total = 20
else:
    total = 25

toppings1 = input("Do you want to add mushrooms on your pizza?(Y or N) ")
toppings2 = input("Do you want to add cheese on your pizza?(Y or N) ")

if toppings1 == 'Y' or toppings1 == 'y':
    if size == 'S' or size == 's':
        total += 2
    else:
        total += 3

if toppings2 == 'Y' or toppings2 == 'y':
    total += 1

print(f"Your final bill is ${total}")
