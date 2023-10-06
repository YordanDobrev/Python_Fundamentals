#Read User Input
numbers = int(input())

current_list = []
filtered_list = []

#Logic

for i in range(numbers):
    current_number = int(input())
    current_list.append(current_number)

command = input()

if command == "even":
    for j in current_list:
        if j % 2 == 0:
            filtered_list.append(j)
elif command == "odd":
    for k in current_list:
        if k % 2 != 0:
            filtered_list.append(k)
elif command == "negative":
    for l in current_list:
        if l < 0:
            filtered_list.append(l)
elif command == "positive":
    for m in current_list:
        if m >= 0:
            filtered_list.append(m)

#Print Output

print(filtered_list)