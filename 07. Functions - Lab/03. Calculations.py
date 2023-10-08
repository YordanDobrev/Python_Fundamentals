#Read User Input
input_operator = input()
first_number = int(input())
second_number = int(input())

#Logic


def calculator(operator, n1, n2):
    if operator == "multiply":
        return n1 * n2
    elif operator == "divide":
        return int(n1 / n2)
    elif operator == "add":
        return n1 + n2
    elif operator == "subtract":
        return n1 - n2


def dictionary_calculator(operator, n1, n2):
    return {
        "multiply": n1 * n2,
        "divide": int(n1 / n2),
        "add": n1 + n2,
        "subtract": n1 - n2
    }.get(operator, "Invalid operator")


#Print Output

print(dictionary_calculator(input_operator, first_number, second_number))