#CALCULATOR

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def modulus(a, b):
    return a % b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulus,
}

def calculator():
    should_accumulate = True
    num1 = float(input("What's the first number?: "))

    while should_accumulate:

        for sym in operations:
            print(sym)

        op = input("Pick an operation:")
        while op not in ["+", "-", "*", "/", "%"]:
            print("Please enter a valid operation!")
            for sym in operations:
                print(sym)

        num2 = float(input("What's the next number?: "))

        out = operations[op](num1, num2)

        print(f"{num1} {op} {num2} = {out}")

        choice = input(f"Type 'y' to continue calculating with {out} or type 'n' to start new calculation")

        while choice.lower() not in ['y', 'n']:
            print("Enter a valid choice!")
            choice = input(f"Type 'y' to continue calculating with {out} or type 'n' to start new calculation: ")

        if choice.lower() == 'y':
            num1 = out
        else:
            should_accumulate = False

            print("\n"*100)
            calculator()


calculator()
