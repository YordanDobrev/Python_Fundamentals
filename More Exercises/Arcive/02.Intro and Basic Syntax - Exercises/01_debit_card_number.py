def digit_check(num):
    if len(num) < 4:
        zeros = (4 - len(num)) * "0"
        return zeros + num
    return num


first_line = input()
second_line = input()
third_line = input()
forth_line = input()

print(f"{digit_check(first_line)} {digit_check(second_line)} {digit_check(third_line)} {digit_check(forth_line)}")