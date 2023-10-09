# Read User Input
string = input().split("|")

new_list = []
latest_list = []
# Logic

for num in range(len(string) - 1 , -1 , -1):
    current_value = string[num].split()
    new_list.append(current_value)
    for i in range(len(current_value)):
        latest_list.append(current_value[i])

# Print Output

print(*latest_list)