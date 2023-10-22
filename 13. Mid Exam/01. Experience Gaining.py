# Read User Input
experience_need = float(input())
battles = int(input())


# Logic
count = 0

for i in range(1, battles + 1):
    current_battle = float(input())

    if i % 3 == 0:
        experience_need -= current_battle * 1.15
    elif i % 5 == 0:
        experience_need -= current_battle * 0.90
        if i % 3 == 0:
            experience_need -= current_battle * 0.95
    else:
        experience_need -= current_battle

    count += 1

    if experience_need <= 0:
        break

# Print Output

if experience_need <= 0:
    print(f"Player successfully collected his needed experience for {count} battles.")
else:
    print(f"Player was not able to collect the needed experience, {experience_need:.2f} more needed.")