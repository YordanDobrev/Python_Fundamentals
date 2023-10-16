#Read User Input
snowballs = int(input())


max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

#Logic

for current_snowball in range(snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    value = (snowball_weight / snowball_time) ** snowball_quality

    if value > max_value:
        max_value = value
        max_weight = snowball_weight
        max_time = snowball_time
        max_quality = snowball_quality

#Print Output

print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")