#Read User Input
list = input().split()
numbers_to_delete = int(input())

converted_list = []

#Logic

for i in list:
    converted_list.append(int(i))

for j in range(numbers_to_delete):
    converted_list.remove(min(converted_list))

#Print Output

print(*converted_list, sep=", ")