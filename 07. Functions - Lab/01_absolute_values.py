#Read User Input
numbers = input().split()

#Logic

new_list = []

for i in range(len(numbers)):
    new_list.append(abs(float(numbers[i])))

#Print Output

print(new_list)