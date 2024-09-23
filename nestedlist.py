def sum_expenses(expenses):

    total = 0
    for item in expenses:
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):

            total += sum_expenses(item)
    return total


input_expenses = eval(input("Enter the nested list of expenses: "))


total_sum = sum_expenses(input_expenses)


print("Total sum of expenses:", total_sum)