from check import Expenses


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
    data=[]
    sum = 0
    for i in Expenses:
        for j in i.split():
            data.append(j)
    for i in range(1, len(data), 2):
        sum += float(data[i])
    print(f"Total expenses: {sum}")
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

    