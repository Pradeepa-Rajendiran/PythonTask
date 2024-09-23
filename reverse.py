def reverse_list(lst):

    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:

        return [lst[-1]] + reverse_list(lst[:-1])


input_transactions = input("Enter the list of transactions: ").split()


try:
    input_transactions = [int(x) for x in input_transactions]
except ValueError:
    pass


reversed_transactions = reverse_list(input_transactions)

print(reversed_transactions)