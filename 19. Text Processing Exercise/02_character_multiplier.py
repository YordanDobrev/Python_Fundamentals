line = input().split()
total = 0

left_part = line[0]
right_part = line[1]

if len(left_part) > len(right_part):
    for index in range(len(right_part)):
        total += ord(left_part[index]) * ord(right_part[index])
    for left_rest_char in range(len(right_part), len(left_part)):
        total += ord(left_part[left_rest_char])

elif len(left_part) < len(right_part):
    for index in range(len(left_part)):
        total += ord(left_part[index]) * ord(right_part[index])
    for rest_char in range(len(left_part), len(right_part)):
        total += ord(right_part[rest_char])


elif len(left_part) == len(right_part):
    for index in range(len(left_part)):
        total += ord(left_part[index]) * ord(right_part[index])
print(total)
