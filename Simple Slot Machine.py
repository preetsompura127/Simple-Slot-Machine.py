import random

class SlotMachine:
    def __init__(self):
        self.balance = 1000
        self.symbols = ["$10", "$100", "$50", "$500"]
        self.payouts = {symbol: 7 for symbol in self.symbols}

    def spin(self):
        roll1 = random.choice(self.symbols)
        roll2 = random.choice(self.symbols)
        roll3 = random.choice(self.symbols)
        return roll1, roll2, roll3

    def check_win(self, roll):
        if roll[0] == roll[1] == roll[2]:
            return "Jackpot!"
        else:
            return "Loss"

    def play(self):
        while True:
            bet = int(input("Enter Bet (1-100): "))
            if bet > self.balance:
                print("Insufficient balance. Try again.")
                continue
            roll= self.spin()
            print(f"Spinning roll: {roll}")
            result = self.check_win(roll)
            print(result)
            if result == "Jackpot!":
                self.balance += 1000
                print(f"New balance: {self.balance}")
            else:
                self.balance -= bet
                print(f"New balance: {self.balance}")
            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                break

SlotMachine().play()
