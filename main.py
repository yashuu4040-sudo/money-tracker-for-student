from income import add_income
from expenses import add_expense, view_transactions, delete_transaction
from budget import set_budget, check_budget
from savings import set_goal, check_goal
from reports import show_balance, category_report, monthly_report
from storage import load_data, save_data


def main():
    data = load_data()

    while True:
        print("\n===== STUDENT MONEY TRACKER =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Delete Transaction")
        print("5. Show Balance")
        print("6. Category Report")
        print("7. Set Budget")
        print("8. Check Budget")
        print("9. Set Savings Goal")
        print("10. Check Savings Goal")
        print("11. Monthly Report")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_income(data)
            save_data(data)
        elif choice == "2":
            add_expense(data)
            save_data(data)
        elif choice == "3":
            view_transactions(data)
        elif choice == "4":
            delete_transaction(data)
            save_data(data)
        elif choice == "5":
            show_balance(data)
        elif choice == "6":
            category_report(data)
        elif choice == "7":
            set_budget(data)
            save_data(data)
        elif choice == "8":
            check_budget(data)
        elif choice == "9":
            set_goal(data)
            save_data(data)
        elif choice == "10":
            check_goal(data)
        elif choice == "11":
            monthly_report(data)
        elif choice == "12":
            print("Thank you for using Student Money Tracker!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 12.")


if __name__ == "__main__":
    main()
