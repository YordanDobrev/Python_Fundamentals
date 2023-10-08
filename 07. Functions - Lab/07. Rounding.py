# Read User Input
given_list = input().split()

# Logic

final_list = []

for i in range(len(given_list)):
    current_value = float(given_list[i])
    final_list.append(round(current_value))

# Print Output

print(final_list)