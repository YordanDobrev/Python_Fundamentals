# Read User Input
numbers = input().split()
filtered_list = []

# Logic

for num in numbers:
    current_num = int(num)
    if current_num < 0:
        continue
    else:
        filtered_list.append(current_num)

# Print Output
if len(filtered_list) == 0:
    print("empty")
else:
    print(*filtered_list[::-1])