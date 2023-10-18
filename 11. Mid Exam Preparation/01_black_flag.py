def pirates_plunder(day, plunder, expected_plunder):
    total = 0

    for i in range(1, day + 1):
        total += plunder

        if i % 3 == 0:
            total += 0.5 * plunder

        if i % 5 == 0:
            total -= 0.3 * total

    if total >= expected_plunder:
        print(f"Ahoy! {total:.2f} plunder gained.")
    else:
        percentage = (total / expected_plunder) * 100
        print(f"Collected only {percentage:.2f}% of the plunder.")


# Read User Input
days = int(input())
plunder_per_day = int(input())
target = float(input())

# Print Output
pirates_plunder(days, plunder_per_day, target)
