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
        print("\n")
        continue
    if not check_user_input(userInput):
        continue
    newMachine.check_all(userInput)
