startMoney = int(input("Starting money\n"))
def transfer():
    p1m, p2m, p3m, p4m , p5m, p6m, p7m, p8m , bank = startMoney, startMoney, startMoney, startMoney, startMoney, startMoney, startMoney, startMoney, 25580

    while True:
        print("player 1 has",p1m,"player 2 has", p2m,"player 3 has", p3m, "player 4 has",p4m,"player 5 has", p5m ,"player 6 has", p6m , "player 7 has",p7m , "player 8 has",p8m ,"Money in the bank" , bank)
        try:
            transferFrom = int(input("Transfer from? (1-8)9 is bank\n"))
            transferTo = int(input("Transfer to? (1-8)9 is bank \n"))
            amount = int(input("Amount?\n"))

            if transferFrom == transferTo or transferFrom not in range(1, 10) or transferTo not in range(1, 10):
                print("Invalid input. Please try again.")
                continue

            players = [p1m, p2m, p3m, p4m, p5m, p6m, p7m, p8m , bank]
            if amount > players[transferFrom - 1]:
                print("Sadly, you do not have enough right now for that.")
                continue

            # Update balances
            players[transferFrom - 1] -= amount
            players[transferTo - 1] += amount
            p1m, p2m, p3m, p4m ,p5m, p6m, p7m, p8m , bank = players  # Update the balances back from the list

        except ValueError:
            print("Please enter valid integers for players and amount.")
            continue

transfer()


