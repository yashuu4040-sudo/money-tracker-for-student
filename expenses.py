def add_expense(data):
    print("\n--- ADD EXPENSE ---")

    try:
        amount = float(input("Enter expense amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category: ")
        description = input("Enter description: ")

        if category.strip() == "":
            print("Category cannot be empty.")
            return

        data["transactions"].append({
            "type": "Expense",
            "amount": amount,
            "category": category,
            "description": description
        })

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid number.")


def view_transactions(data):
    print("\n--- TRANSACTION HISTORY ---")

    if len(data["transactions"]) == 0:
        print("No transactions found.")
        return

    for i, transaction in enumerate(data["transactions"], 1):
        print(
            i, "|", transaction["type"],
            "| ₹", transaction["amount"],
            "|", transaction["category"],
            "|", transaction["description"]
        )


def delete_transaction(data):
    view_transactions(data)

    if len(data["transactions"]) == 0:
        return

    try:
        number = int(input("Enter transaction number to delete: "))

        if 1 <= number <= len(data["transactions"]):
            removed = data["transactions"].pop(number - 1)
            print("Deleted:", removed["description"])
        else:
            print("Invalid transaction number.")

    except ValueError:
        print("Please enter a valid number.")
