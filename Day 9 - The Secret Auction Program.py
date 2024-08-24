#THE SECRET AUCTION PROGRAM

bids = {}
continue_bidding = True

def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ''
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of {highest_bid}")


name = input("What's your name?:  ")
price = int(input("What's your bid?: $"))

while continue_bidding:

    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        find_highest_bidder(bids)
        break
    else:
        print("\n"*100)
        name = input("What's your name?:  ")
        price = int(input("What's your bid?: $"))
