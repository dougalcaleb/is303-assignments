collecting_values = True
expenses = []

while collecting_values:
    input_str = input("Enter an expense (or 0 to finish): ")

    # use try/catch to ensure that the input is a valid number (catches all possibilities I believe)
    try:
        parsed_num = float(input_str)
    except:
        print("Invalid input")
        continue

    # negative expenses don't make sense in this case, disallow them
    if parsed_num < 0:
        print("Invalid input, number must be greater than or equal to 0")
        continue

    # if 0 entered, exit collection, otherwise add the expense
    if parsed_num == 0:
        collecting_values = False
    else:
        expenses.append(parsed_num)

# count the number of expenses in each size category
small_expenses = sum(1 for x in expenses if x < 25)
med_expenses = sum(1 for x in expenses if x >= 25 and x <= 100)
large_expenses = sum(1 for x in expenses if x > 100)

# print results
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