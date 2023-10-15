# Read User Input
numbers = [int(number) for number in input().split(", ")]

# Logic

group = 10

while numbers:
    current_group = [the_group for the_group in numbers if the_group <= group]
    print(f"Group of {group}'s: {current_group}")
    group += 10
    numbers = [num for num in numbers if num not in current_group]

# Print Output
