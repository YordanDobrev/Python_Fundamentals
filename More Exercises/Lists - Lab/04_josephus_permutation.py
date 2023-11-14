circle = input().split()
skip = int(input())

new_list = []
counter = 0

index = 0
while len(circle) > 0:
    counter += 1

    if counter % skip == 0:
        new_list.append(int(circle.pop(index)))
    else:
        index += 1

    if index >= len(circle):
        index = 0

print(str(new_list).replace(' ', '').replace('\'', ''))
