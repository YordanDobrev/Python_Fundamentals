def sum_numbers(n1: int, n2: int) -> int:
    return n1 + n2


def subtract(summed_numbers: int, n3: int) -> int:
    return summed_numbers - n3


def add_and_subtract(first: int, second: int, third) -> int:
    result = sum_numbers(first, second)
    final_result = subtract(result, third)
    return final_result


# Read User Input
first_num = int(input())
second_num = int(input())
third_num = int(input())

# Print Output

print(add_and_subtract(first_num, second_num, third_num))
