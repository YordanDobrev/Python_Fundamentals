#Read User Input
number = int(input())
word = input()

original_list = []

#Logic

for i in range(number):
    current_string = input()
    original_list.append(current_string)

filtered_list = []

for j in original_list:
    if word in j:
        filtered_list.append(j)

#Print Output

print(original_list)
print(filtered_list)