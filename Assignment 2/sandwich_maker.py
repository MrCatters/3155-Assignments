import data


class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.__machine_resources = machine_resources

    @staticmethod
    def display_resources():
        resources = data.resources
        print(f'You have:')
        print(f'{resources["bread"]} slices of bread.')
        print(f'{resources["ham"]} slices of ham.')
        print(f'{resources["cheese"]} ounces of cheese.')

    def check_resources(self, sandwich_size):
        recipes = data.recipes[sandwich_size]["ingredients"]
        if self.__machine_resources["bread"] - recipes["bread"] < 0:
            print("Sorry there is not enough bread.")
            return False
        if self.__machine_resources["ham"] - recipes["ham"] < 0:
            print("Sorry there is not enough ham.")
            return False
        if self.__machine_resources["cheese"] - recipes["cheese"] < 0:
            print("Sorry there is not enough ham.")
            return False
        return True

    def make_sandwich(self, sandwich_size):
        size_resources = data.recipes[sandwich_size]["ingredients"]
        self.__machine_resources["bread"] -= size_resources["bread"]
        self.__machine_resources["ham"] -= size_resources["ham"]
        self.__machine_resources["cheese"] -= size_resources["cheese"]
        print(f"A {sandwich_size} sandwich was made!")
