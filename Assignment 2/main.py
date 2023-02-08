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


def main():
    while True:
        user_input = input("What would you like? (small/ medium/ large/ off/ report)")

        if user_input == "off":
            break
        if user_input == "report":
            sandwich_maker_instance.display_resources()
            continue
        if not check_user_input(user_input):
            continue
        if sandwich_maker_instance.check_resources(user_input):
            sandwich_cost = recipes[user_input]["cost"]
            money_held = cashier_instance.process_coins()

            if cashier_instance.transaction_result(money_held, sandwich_cost):
                sandwich_maker_instance.make_sandwich(user_input)


if __name__ == "__main__":
    main()
