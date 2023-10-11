def loading_bar(number_to_use):
    real_number = number_to_use // 10
    rest_of_number = 10 - real_number

    if number_to_use == 100:
        return f"{number_to_use}% Complete!\n[{real_number * '%'}]"

    return f"{number_to_use}% [{(real_number * '%')}{rest_of_number*'.'}]\nStill loading..."


# Read User Input
num = int(input())

# Logic

result = loading_bar(num)

# Print Output

print(result)
