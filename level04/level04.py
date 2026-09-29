last_input = -1
expenses = []

while last_input != 0:
    last_input = float(input("Enter an expense (or 0 to finish): "))

    if last_input != 0:
        expenses.append(last_input)

small_expenses = sum(1 for x in expenses if x < 25)
med_expenses = sum(1 for x in expenses if x >= 25 and x <= 100)
large_expenses = sum(1 for x in expenses if x > 100)

print(" ")
print("Expense Summary")
print("---------------")
print(f"Number of expenses: {len(expenses)}")
print(f"Total: ${sum(expenses):.2f}")
print(f"Average: ${sum(expenses) / len(expenses):.2f}")
print(f"Smallest expense: ${min(expenses):.2f}")
print(f"Largest expense: ${max(expenses):.2f}")
print(" ")
print(f"Small expenses: {small_expenses}")
print(f"Medium expenses: {med_expenses}")
print(f"Large expenses: {large_expenses}")