def add_income(data):
    print("\n--- ADD INCOME ---")

    try:
        amount = float(input("Enter income amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        source = input("Enter source of income: ")

        if source.strip() == "":
            print("Source cannot be empty.")
            return

        data["transactions"].append({
            "type": "Income",
            "amount": amount,
            "category": source,
            "description": "Income"
        })

        print("Income added successfully!")

    except ValueError:
        print("Please enter a valid number.")
