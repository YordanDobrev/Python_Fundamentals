#Read User Input
factor = int(input())
count = int(input())

#Logic

final_list = []

for i in range(1, count + 1):
    current_number = factor * i
    final_list.append(current_number)

#Print Output

print(final_list)