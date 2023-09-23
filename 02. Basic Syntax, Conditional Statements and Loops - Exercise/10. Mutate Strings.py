#Read User Input
first_string = input()
second_string = input()

last_string = first_string

#Logic

for i in range(len(first_string)):
    current_string = ""
    left_part = second_string[:i+1]
    right_part = first_string[i+1:]
    current_string += left_part + right_part

    if current_string == last_string:
        continue
    last_string = current_string
    print(current_string)

#Print Output

