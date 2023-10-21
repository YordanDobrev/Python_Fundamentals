from math import ceil

# Read User Input
number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

# Logic

max_bonus = 0
max_lecture = 0

for i in range(number_of_students):
    current_attendances = int(input())
    total_bonus = current_attendances / number_of_lectures * (5 + additional_bonus)
    if max_bonus <= total_bonus:
        max_bonus = total_bonus
        max_lecture = current_attendances

# Print Output

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {max_lecture} lectures.")