
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

    @staticmethod
    def display_resources():
        resources = SandwichDataModel.resources
        print(f'You have:')
        print(f'{resources["bread"]} slices of bread.')
        print(f'{resources["ham"]} slices of ham.')
        print(f'{resources["cheese"]} ounces of cheese.')

    def make_sandwich(self, sandwich_size):
        size_resources = SandwichDataModel.recipes[sandwich_size]["ingredients"]
        self.machine_resources["bread"] -= size_resources["bread"]
        self.machine_resources["ham"] -= size_resources["ham"]
        self.machine_resources["cheese"] -= size_resources["cheese"]

    def check_all(self, sandwich_size):
        if self.check_resources(sandwich_size):
            sandwich_cost = SandwichDataModel.recipes[sandwich_size]["cost"]
            if transaction_result(process_coins(), sandwich_cost):
                self.make_sandwich(sandwich_size)
                print(f"A {sandwich_size} sandwich was made!")
                return
            print("Not enough money!")
            return
        print("Not enough resources!")
