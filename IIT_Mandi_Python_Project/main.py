
import os
from datetime import datetime

EXPENSES_FILE = "expenses.txt"

def add_expense(category, amount, date):
    with open(EXPENSES_FILE, "a") as file:
        file.write(f"{category},{amount},{date}\n")
    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists(EXPENSES_FILE):
        print("No expenses recorded.")
        return

    expenses = {}
    with open(EXPENSES_FILE, "r") as file:
        for line in file:
            category, amount, date = line.strip().split(',')
            if category not in expenses:
                expenses[category] = []
            expenses[category].append((amount, date))
    
    print("Expenses:")
    for category, items in expenses.items():
        print(f"{category}:")
        for i, (amount, date) in enumerate(items):
            print(f"  {i+1}. Amount: {amount} - Date: {date}")

def monthly_summary(year, month):
    if not os.path.exists(EXPENSES_FILE):
        print("No expenses recorded.")
        return

    total_expenses = 0
    category_expenses = {}

    with open(EXPENSES_FILE, "r") as file:
        for line in file:
            try:
                category, amount, date = line.strip().split(',')
                amount = float(amount)
                expense_date = datetime.strptime(date, "%Y-%m-%d")
                if expense_date.year == year and expense_date.month == month:
                    total_expenses += amount
                    if category not in category_expenses:
                        category_expenses[category] = 0
                    category_expenses[category] += amount
            except ValueError:
                print(f"Skipping line due to error: {line.strip()}")
                continue

    print(f"Monthly Summary ({datetime(year, month, 1).strftime('%B %Y')}):")
    print(f"Total Expenses: {total_expenses}")
    print("By Category:")
    for category, amount in category_expenses.items():
        print(f"{category}: {amount}")

def main():
    while True:
        print("\nWelcome to Personal Expense Tracker!")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category (e.g., Food, Travel): ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(category, amount, date)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            year = int(input("Enter year (YYYY): "))
            month = int(input("Enter month (MM): "))
            monthly_summary(year, month)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

