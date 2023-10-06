#Read User Input
numbers = input().split()

#Logic

reverted_list = []

for i in numbers:
    current_number = -int(i)
    reverted_list.append(current_number)

#Print Output

print(reverted_list)