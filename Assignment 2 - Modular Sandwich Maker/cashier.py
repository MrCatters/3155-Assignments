class Cashier:
    def __init__(self):
        pass

    @staticmethod
    def process_coins():
        print("How many:")
        total = 0
        total += int(input("Dollars? "))
        total += .5 * int(input("Half dollars? "))
        total += .25 * int(input("Quarters? "))
        total += .05 * int(input("Nickels? "))
        return float(total)

    @staticmethod
    def transaction_result(coins, sandwich_cost):
        change = float(coins - sandwich_cost)
        if change >= 0:
            print(f"Here is {change} in change!")
            return True
        print("Not enough money!")
        return False