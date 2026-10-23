import argparse
import json
FILE ="expenses.json"

class Expense:
    def __init__(self, item, amount):
        self.item = item
        self.amount = amount
    def to_dict(self):
        return{"item": self.item, "amount": self.amount}
    
def load_expenses():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            return [Expense(expense["item"], expense["amount"]) for expense in data]
    except(FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open(FILE, 'w') as f:
        json.dump([expense.to_dict() for expense in expenses], f, indent=2)

expenses = load_expenses()
def add_expense(item, amount):
    expenses.append(Expense(item, amount))
    save_expenses(expenses)
    print("Expense added successfully.")

def add_expenses():
    item = input("Enter an item name:")
    while True:
        try:
            amount = float(input("Enter the amount:"))
            break
        except ValueError:
            print("Please enter a vaild number .")
    add_expense(item, amount)

def view_expenses():
    if not expenses:
        print("No expenses found.")
    else:
        for number, expense in enumerate(expenses, start=1):
            print(f"{number}. {expense.item}: {expense.amount}")

def show_total():
    total = sum(expense.amount for expense in expenses)
    print(f"Total expenses: {total}")

def delete_expense_by_number(choice):
    if 1 <= choice <= len(expenses):
        deleted_expense = expenses.pop(choice-1)
        save_expenses(expenses)
        print(f"Expense deleted :{deleted_expense.item}")
    else:
        print("Invalid choice.")

def delete_expense():
    if not expenses:
        print("no expense to delete.")
        return
    for number,expense in enumerate(expenses, start=1):
        print(f"{number}.{expense.item}: {expense.amount}")
    try:
        choice = int(input("Enter the number of the expense to delete: "))
    except ValueError:
        print("Please enter a valid number.")

def run_menu():
    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total")
        print("4. Delete expense")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def build_parser():
    parser = argparse.ArgumentParser(description="Simple expense tracker")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add an expense")
    add_parser.add_argument("item", help="What you spent money on")
    add_parser.add_argument("amount", type=float, help="How much you spent")

    subparsers.add_parser("list", help="Show all expenses")
    subparsers.add_parser("total", help="Show the total spent")

    delete_parser = subparsers.add_parser("delete", help="Delete an expense by its number")
    delete_parser.add_argument("number", type=int, help="number shown by the list command")

    return parser

def run_command(args):
    if args.command == "add":
        add_expense(args.item, args.amount)
    elif args.command == "list":
        view_expenses()
    elif args.command == "total":
        show_total()
    elif args.command == "delete":
        delete_expense_by_number(args.number)


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.command is None:
        run_menu()
    else:
        run_command(args)

if __name__ == "__main__":
    main()