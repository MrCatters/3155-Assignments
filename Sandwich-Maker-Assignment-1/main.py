from SandwichMachine import SandwichMachine
import SandwichDataModel


def check_user_input(user_input):
    for sandwich in SandwichDataModel.recipes:
        if user_input == sandwich:
            return True
    print("Incorrect option selected.")
    print("Please try again.")
    print("\n")
    return False


while True:
    newMachine = SandwichMachine(SandwichDataModel.resources)
    userInput = input("What would you like? (small/ medium/ large/ off/ report)")

    if userInput == "off":
        break
    if userInput == "report":
        newMachine.display_resources()
        continue
    if not check_user_input(userInput):
        continue
    if newMachine.check_resources(userInput):
        sandwich_cost = SandwichDataModel.recipes[userInput]["cost"]
        money_held = newMachine.process_coins()

        if newMachine.transaction_result(money_held, sandwich_cost):
            newMachine.make_sandwich(userInput)
