def set_goal(data):
    print("\n--- SET SAVINGS GOAL ---")

    try:
        amount = float(input("Enter savings goal: ₹"))

        if amount <= 0:
            print("Goal must be greater than zero.")
            return

        data["savings_goal"] = amount
        print("Savings goal saved!")

    except ValueError:
        print("Please enter a valid number.")


def check_goal(data):
    print("\n--- SAVINGS GOAL STATUS ---")

    if data["savings_goal"] == 0:
        print("Please set a savings goal first.")
        return

    income = 0
    expense = 0

    for transaction in data["transactions"]:
        if transaction["type"] == "Income":
            income += transaction["amount"]
        else:
            expense += transaction["amount"]

    savings = income - expense

    print("Goal    : ₹", data["savings_goal"])
    print("Savings : ₹", savings)

    if savings >= data["savings_goal"]:
        print("Savings goal achieved!")
    else:
        print("Still needed: ₹", data["savings_goal"] - savings)
