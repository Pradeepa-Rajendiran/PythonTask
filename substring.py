main_string = input("Enter the input string")
unique_substrings = set()

for i in range(len(main_string)):
    for j in range(i + 1, len(main_string) + 1):
        unique_substrings.add(main_string[i:j])

count = len(unique_substrings)
print('Total unique substrings:' ,count)


def rearrange_vowels_descending(s):
    vowels="aeiouAEIOU"
    extraxted_vowels=[char for char in s if char in vowels]
    extraxted_vowels.sort(reverse=True)
    vowel_iter=iter(extraxted_vowels)
    result=''.join(next(vowel_iter) if char in vowels else char for char in s)
    return result
input_string=input("Enter the input string")
output_string=rearrange_vowels_descending(input_string)
print("Rearranged string:",output_string)