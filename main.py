import json
FILE ="expenses.json"
def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except(FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open(FILE, 'w') as f:
        json.dump(expenses,f, indent=2)

expenses = load_expenses()
def add_expenses():
    item = input("Enter an item name:")
    while True:
        try:
            amount = float(input("Enter the amount:"))
            break
        except ValueError:
            print("Please enter a valid number .")
    expenses.append({"item": item, "amount": amount})
    save_expenses(expenses)
    print("Expense added successfully.")

def view_expenses():
    if not expenses :
        print("No expenses found.")
    else:
        for expense in expenses:
            print(f"Item: {expense['item']}")
            print(f"Amount: {expense['amount']}")

def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: {total}")
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()