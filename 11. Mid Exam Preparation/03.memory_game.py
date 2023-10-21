def main():
    elements = input().split()
    moves = 0

    while True:
        moves += 1
        command = input()

        if command == "end":
            print(f"Sorry you lose :(\n{' '.join(elements)}")
            break
        first_index, second_index = map(int, command.split())

        if invalid(first_index, second_index, elements):
            handle_invalid(elements, moves)
        else:
            valid(first_index, second_index, elements, moves)


def valid(first_index, second_index, elements, moves_counter):
    if elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        second_element = elements[second_index]
        elements.pop(first_index)
        elements.remove(second_element)
    else:
        print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {moves_counter} turns!")
        exit()


def handle_invalid(all_elements, move_counter):
    mid_index = len(all_elements) // 2
    all_elements.insert(mid_index, f"-{move_counter}a")
    all_elements.insert(mid_index, f"-{move_counter}a")
    print("Invalid input! Adding additional elements to the board")


def invalid(index1, index2, the_elements):
    return (
        index1 == index2
        or index1 < 0
        or index2 < 0
        or index1 >= len(the_elements)
        or index2 >= len(the_elements)
    )


main()