#Read User Input
year = int(input())

#Logic

while True:
    year += 1
    current_year = str(year)
    if len(current_year) == len(set(current_year)):
        break

#Print Output

print(year)