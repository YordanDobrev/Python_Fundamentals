#Read User Input
number = str(input())

#Logic

for i in range(len(number)):
    current_digit = (sorted(number,reverse=True)[i])
    print(current_digit, end="")

#Print Output

