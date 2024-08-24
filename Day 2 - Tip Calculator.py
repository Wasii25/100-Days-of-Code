#TIP CALCULATOR
print("Welcome to the tip calculator!!")

total = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give?? 10, 12 or 15? "))

while tip not in [10, 12, 15]:
    print('Invalid tip. Choose between 10 , 12 and 15 only')
    tip = float(input("How much tip would you like to give?? 10, 12 or 15? "))

split = float(input("How many people would like to split the bill? "))

tip = (tip/100) * total
total = total + tip

print("Each person should pay: $",round(total/split,2))