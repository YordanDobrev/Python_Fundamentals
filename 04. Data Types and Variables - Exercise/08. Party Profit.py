#Read User Input
group_size = int(input())
days = int(input())

#Logic

total_coins = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        group_size -= 2
    if i % 15 == 0:
        group_size += 5

    total_coins += 50 - (group_size * 2)

    if i % 3 == 0:
        total_coins -= (group_size * 3)
    if i % 5 == 0:
        total_coins += (group_size * 20)
        if i % 3 == 0:
            total_coins -= (group_size * 2)

average = int(total_coins / group_size)
#Print Output

print(f"{group_size} companions received {average} coins each.")
