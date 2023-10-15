# Read User Input
electrons = int(input())

# Logic

list_of_electrons = []

for i in range(1, electrons + 1):
    if electrons <= 0:
        break

    formula = 2 * i ** 2

    if electrons >= formula:
        list_of_electrons.append(formula)
        electrons -= formula
        if electrons == 0:
            break
    else:
        list_of_electrons.append(electrons)
        break

# Print Output

print(list_of_electrons)