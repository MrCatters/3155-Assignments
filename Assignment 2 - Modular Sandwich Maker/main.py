import data
from sandwich_maker import SandwichMachine
from cashier import Cashier

resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMachine(resources)
cashier_instance = Cashier()


def check_user_input(user_input):
    for sandwich in recipes:
        if user_input == sandwich:
            return True
    print("Incorrect option selected.")
    print("Please try again.")
    print("\n")
    return False


while True:
    userInput = input("What would you like? (small/ medium/ large/ off/ report)")

    if userInput == "off":
        break
    if userInput == "report":
        sandwich_maker_instance.display_resources()
        continue
    if not check_user_input(userInput):
        continue
    if sandwich_maker_instance.check_resources(userInput):
        sandwich_cost = recipes[userInput]["cost"]
        money_held = cashier_instance.process_coins()

        if cashier_instance.transaction_result(money_held, sandwich_cost):
            sandwich_maker_instance.make_sandwich(userInput)
