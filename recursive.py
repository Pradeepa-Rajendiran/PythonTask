def permute(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    result = []
    for i in range(len(lst)):

        current_element = lst[i]

        remaining_elements = lst[:i] + lst[i+1:]

        for p in permute(remaining_elements):
            result.append([current_element] + p)

    return result

input_list = input("Enter the list of elements : ").split()

try:
    input_list = [int(x) for x in input_list]
except ValueError:
    pass

permutations = permute(input_list)

print(permutations)
