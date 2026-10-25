import argparse
import json
import logging

FILE = "expenses.json"

logger = logging.getLogger(__name__)


class Expense:
    """One spending record: what was bought and how much it cost."""

    def __init__(self, item: str, amount: float) -> None:
        self.item = item
        self.amount = amount

    def to_dict(self) -> dict[str, str | float]:
        """Return the expense as a dictionary that can be saved as JSON."""
        return {"item": self.item, "amount": self.amount}


def load_expenses() -> list[Expense]:
    """Read expenses from FILE; return an empty list if it is missing or broken."""
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            return [Expense(expense["item"], expense["amount"]) for expense in data]
    except FileNotFoundError:
        logger.info("%s not found, starting with no expenses", FILE)
        return []
    except json.JSONDecodeError:
        logger.warning("%s is not valid JSON, starting with no expenses", FILE)
        return []


def save_expenses(expenses: list[Expense]) -> None:
    """Write the given expenses to FILE as JSON."""
    with open(FILE, "w") as f:
        json.dump([expense.to_dict() for expense in expenses], f, indent=2)
    logger.info("Saved %d expenses to %s", len(expenses), FILE)


expenses: list[Expense] = load_expenses()


def add_expense(item: str, amount: float) -> None:
    """Add one expense to the list and save it."""
    expenses.append(Expense(item, amount))
    logger.info("Add expense: %s (%s)", item, amount)
    save_expenses(expenses)
    print("Expense added successfully.")


def add_expenses() -> None:
    """Ask the user for an item and amount, then add the expense."""
    item = input("Enter an item name:")
    while True:
        try:
            amount = float(input("Enter the amount:"))
            break
        except ValueError:
            print("Please enter a vaild number .")
    add_expense(item, amount)


def view_expenses() -> None:
    """Print all expenses with numbers, or a message if there are none."""
    if not expenses:
        print("No expenses found.")
    else:
        for number, expense in enumerate(expenses, start=1):
            print(f"{number}. {expense.item}: {expense.amount}")


def show_total() -> None:
    """Print the total of all expenses."""
    total = sum(expense.amount for expense in expenses)
    print(f"Total expenses: {total}")


def delete_expense_by_number(choice: int) -> None:
    """Delete the expense at position `choice` (starting from 1) and save."""
    if 1 <= choice <= len(expenses):
        deleted_expense = expenses.pop(choice - 1)
        save_expenses(expenses)
        logger.info("Deleted expense: %s", deleted_expense.item)
        print(f"Expense deleted :{deleted_expense.item}")
    else:
        logger.warning(
            "Invalid delete number: %s (have %d expenses)", choice, len(expenses)
        )
        print("Invalid choice.")


def delete_expense() -> None:
    """Show the expenses, ask which one to delete, then delete it."""
    if not expenses:
        print("no expense to delete.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}.{expense.item}: {expense.amount}")
    try:
        choice = int(input("Enter the number of the expense to delete: "))
    except ValueError:
        print("Please enter a valid number.")


def run_menu() -> None:
    """Run the interactive menu until the user chooses Exit."""
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


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser with add, list, total and delete commands."""
    parser = argparse.ArgumentParser(description="Simple expense tracker")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add an expense")
    add_parser.add_argument("item", help="What you spent money on")
    add_parser.add_argument("amount", type=float, help="How much you spent")

    subparsers.add_parser("list", help="Show all expenses")
    subparsers.add_parser("total", help="Show the total spent")

    delete_parser = subparsers.add_parser(
        "delete", help="Delete an expense by its number"
    )
    delete_parser.add_argument(
        "number", type=int, help="number shown by the list command"
    )

    return parser


def run_command(args: argparse.Namespace) -> None:
    """Run the command chosen on the command line."""
    if args.command == "add":
        add_expense(args.item, args.amount)
    elif args.command == "list":
        view_expenses()
    elif args.command == "total":
        show_total()
    elif args.command == "delete":
        delete_expense_by_number(args.number)


def setup_logging() -> None:
    """ "Send log messages to expense_tracker.log."""
    logging.basicConfig(
        filename="expense_tracker.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


def main(argv: list[str] | None = None) -> None:
    """Start the program: use the command line if given, otherwise the menu."""
    setup_logging()
    args = build_parser().parse_args(argv)
    if args.command is None:
        run_menu()
    else:
        run_command(args)


if __name__ == "__main__":
    main()
