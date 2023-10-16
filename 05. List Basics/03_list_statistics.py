#Read User Input
numbers = int(input())

positive_list = []
negative_list = []

#Logic

for i in range(numbers):
    current_value = int(input())
    if current_value >= 0:
        positive_list.append(current_value)
    else:
        negative_list.append(current_value)

#Print Output

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative_list)}")