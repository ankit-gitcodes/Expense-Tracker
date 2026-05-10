def Add_Expense():
    item = input("Enter expense item: ")
    amount = float(input("Enter expense amount: "))
    try:
        file = open("expenses.txt", "a")
    except IOError:
        file = open("expenses.txt", "w")
        file.write(f"{item}: {amount}\n")
    else:            
        file.write(f"{item}: {amount}\n")
    finally:
        file.close()

def View_Expenses():
    try:
        file = open("expenses.txt", "r")
    except IOError:
        print("No expenses to display.")
    else:
        Expenses = file.readlines()
        for expense in Expenses:
            print(expense.strip())
        file.close()
def Show_Total():
    file = open("expenses.txt", "r")
    Expenses = file.readlines()
    t = 0
    sum = 0
    for i in Expenses:
        for j in i.split():
            if j.isdigit():
                t += float(j)
        sum += t
        t = 0
    print(f"Total expenses: {sum+1}")
    file.close()

def Exit():
    print("Exiting the program.")


while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if choice == 1:
        Add_Expense()
    elif choice == 2:
        View_Expenses()
    elif choice == 3:
        Show_Total()
    elif choice == 4:
        Exit()
        break
