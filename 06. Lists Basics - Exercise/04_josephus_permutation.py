# Read User Input
numbers = input().split()
k_number = int(input())
# Logic

the_new_list = []

while True:

    for i in range(len(numbers)):
        the_new_list.append(numbers)
        numbers.pop(i)
        break
    if len(the_new_list) == len(numbers):
        break


# Print Output

print(the_new_list)