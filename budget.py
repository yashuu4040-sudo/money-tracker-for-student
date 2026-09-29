def set_budget(data):
    print("\n--- SET BUDGET ---")

    try:
        amount = float(input("Enter monthly budget: ₹"))

        if amount <= 0:
            print("Budget must be greater than zero.")
            return

        data["budget"] = amount
        print("Budget saved successfully!")

    except ValueError:
        print("Please enter a valid number.")


def check_budget(data):
    print("\n--- BUDGET STATUS ---")

    if data["budget"] == 0:
        print("Please set a budget first.")
        return

    spent = 0

    for transaction in data["transactions"]:
        if transaction["type"] == "Expense":
            spent += transaction["amount"]

    remaining = data["budget"] - spent

    print("Budget   : ₹", data["budget"])
    print("Spent    : ₹", spent)
    print("Remaining: ₹", remaining)

    if remaining < 0:
        print("Warning: You have exceeded your budget!")
    else:
        print("You are within your budget.")
