def speed_time(speed):
    total = 0
    for current_speed in speed:
        if current_speed == 0:
            total *= 0.80
        else:
            total += current_speed
    return total


# Read User Input
numbers = input().split()

# Logic
new_list = len(numbers) // 2
left_part = numbers[0:new_list]
right_part = numbers[new_list + 1:]
first_car = list(map(int, left_part))
second_car = list(map(int, right_part))
sum_1_car = speed_time(first_car)
sum_2_car = speed_time(second_car)

# Print Output

if sum_1_car < sum_2_car:
    print(f"The winner is left with total time: {sum_1_car:.1f}")
else:
    print(f"The winner is right with total time: {sum_2_car:.1f}")
