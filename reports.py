def show_balance(data):
    income = 0
    expense = 0

    for transaction in data["transactions"]:
        if transaction["type"] == "Income":
            income += transaction["amount"]
        else:
            expense += transaction["amount"]

    print("\n--- BALANCE ---")
    print("Total Income : ₹", income)
    print("Total Expense: ₹", expense)
    print("Balance      : ₹", income - expense)


def category_report(data):
    print("\n--- CATEGORY REPORT ---")

    categories = {}

    for transaction in data["transactions"]:
        if transaction["type"] == "Expense":
            category = transaction["category"]

            if category not in categories:
                categories[category] = 0

            categories[category] += transaction["amount"]

    if len(categories) == 0:
        print("No expenses found.")
        return

    for category in categories:
        print(category, ": ₹", categories[category])


def monthly_report(data):
    # This simple version reports all stored transactions.
    print("\n--- FINANCIAL SUMMARY ---")

    income = 0
    expense = 0

    for transaction in data["transactions"]:
        if transaction["type"] == "Income":
            income += transaction["amount"]
        else:
            expense += transaction["amount"]

    print("Income : ₹", income)
    print("Expense: ₹", expense)
    print("Savings: ₹", income - expense)
