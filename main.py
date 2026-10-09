expenses=[]
def add_expense():
    item=input("Enter an item name: ")                                                
    amount=float(input("Enter the amount: "))
    expenses.append({"item": item, "amount": amount})
    print("Expense added successfully.")


def view_expenses():
    if not expenses:
        print("no expenses yet.")
    else:
        for expense in expenses:
            print(f"Item: {expense['item']}")
            print(f"Amount: {expense['amount']}")


def show_total():
    total = sum(e['amount']for e in expenses)
    print(total)
    
def main():
    while True:
        print("\n1. Add expense")
        print("2. View expenses")
        print("3. Show total")
        print("4.Quit")
        choice = input("Enter your choose: ")
        if choice=="1":
            add_expense()
        elif choice=="2":
            view_expenses()
        elif choice=="3":
            show_total()
        elif choice=="4":
            break
        else:
            print("Invaild choice")

if __name__=="__main__":
    main()
