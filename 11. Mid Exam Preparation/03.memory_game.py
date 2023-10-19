def middle(elements):
    middle_index = len(elements) // 2
    elements.insert(middle_index, f"-{counter}a")
    elements.insert(middle_index, f"-{counter}a")
    return elements

def match(numbers, all_elements):
    numbers = numbers.split()

    first_index = int(numbers[0])
    second_index = int(numbers[1])

    if first_index == second_index \
            or first_index < 0 \
            or first_index > len(all_elements) \
            or second_index < 0 \
            or second_index > len(all_elements):
        middle(all_elements)
        print(f"Invalid input! Adding additional elements to the board")

    elif all_elements[first_index] == all_elements[second_index]:
        matched_pair = all_elements[first_index]
        all_elements.remove(all_elements[first_index])
        all_elements.remove(all_elements[second_index])
        print(f"Congrats! You have found matching elements - ${matched_pair}!")

    elif first_index in all_elements != second_index in all_elements:
        print("Try again!")

    elif len(all_elements) == 0:
        print(f"You have won in {counter} turns!")
        exit()


# Read User Input
sequence_of_elements = input().split()
command = input()

# Logic
counter = 0

while command != "end":
    counter += 1
    current_pair = command
    match(current_pair, sequence_of_elements)
    command = input()
    if command == "end":
        print(f"Sorry you lose :( \n"
              f"{' '.join(sequence_of_elements)}")
        break

# Print Output
