
import SandwichDataModel


def transaction_result(coins, sandwich_cost):
    return float(coins - sandwich_cost) >= 0


def process_coins():
    print("How many:")
    total = 0
    total += int(input("Dollars? "))
    total += .5 * int(input("Half dollars? "))
    total += .25 * int(input("Quarters? "))
    total += .05 * int(input("Nickels? "))
    return float(total)


class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, sandwich_size):
        recipes = SandwichDataModel.recipes[sandwich_size]["ingredients"]
        if self.machine_resources["bread"] - recipes["bread"] < 0:
            print("Sorry there is not enough bread.")
            return False
        if self.machine_resources["ham"] - recipes["ham"] < 0:
            print("Sorry there is not enough ham.")
            return False
        if self.machine_resources["cheese"] - recipes["cheese"] < 0:
            print("Sorry there is not enough ham.")
            return False
        return True
