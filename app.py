from expense import Expense

def main():
    print(f"----------Expense Tracker!----------\n")
    expense = getInput()
    print(expense)
    
    expenseFile = "expenses.csv"
    saveToFile(expense, expenseFile)

    totalBudget = 30000
    summaryOfExpenses(expenseFile, totalBudget)
    

def getInput():
    print("-->Getting your input...")
    expenseName = input("Enter expense name:")
    expenseAmount = float(input("Enter expense amount:"))
    
    print(f"Your expense name: {expenseName}\nYour expense amount: {expenseAmount}")

    expenseCategories = [
        "Food", "Home", "Work", "Fun", "Other"
        ]
    while True:
        print("Select your category:")
        for i, categoryName in enumerate(expenseCategories):
            print(f"    {i+1}. {categoryName}")

        valueRange = f"[1 - {len(expenseCategories)}]"
        selected = int(input(f"Enter catory's number {valueRange}:"))

        if selected-1 in range(0,len(expenseCategories)):
            selectedCategory = expenseCategories[selected-1]
            # print(selectedCategory)
            newExpense = Expense(
                name=expenseName, 
                category=selectedCategory,
                amount=expenseAmount
                )
            return newExpense
        else:
            print("Invalid Category!")
            
def saveToFile(expense: Expense, filename):
    print(f"-->Saving Your Expense: {expense} to {filename} ")
    with open(filename, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

    print("Saved !")
    
def summaryOfExpenses(fileName, budget):
    print("--> Summary of Your Expenses....\n")
    expenses: list[Expense] = []
    with open(fileName, "r") as f:
        readExpenses = f.readlines()
        for line in readExpenses:
            # print(line)
            exName, exAmount, exCategory = line.strip().split(",")
            thisExpense = Expense(name=exName, amount=float(exAmount), category=exCategory)
            # print(thisExpense)
            expenses.append(thisExpense)
    # print(expenses)

    amountByCategory = {}
    for expense in expenses:
        key = expense.category
        if key in amountByCategory:
            amountByCategory[key] += expense.amount
        else:
            amountByCategory[key] = expense.amount
    # print(amountByCategory)
    print("----------Expense By Category----------")
    for key, amount in amountByCategory.items():
        print(f">> {key} : Rs.{amount}")

    print("\n----------Budget----------")
    totalSpent = sum([ex.amount for ex in expenses])
    print(f"Total Spent: Rs.{totalSpent:.2f}")
    print(f"Remaining Budget: Rs.{budget - totalSpent:.2f}")




if __name__ == "__main__":  # only true when you run this file directly
    main()  # to run it
