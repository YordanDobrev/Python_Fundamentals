# Read User Input
string = input()

# Logic

#exclusive_list = ['a', 'o', 'u', 'e', 'i']

final_result = [the_list for the_list in string if the_list.lower() not in ['a', 'o', 'u', 'e', 'i']]

# Print Output

print("".join(final_result))
