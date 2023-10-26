# Read User Input
fire = input().split("#")
water = int(input())

# Logic
total_fire = 0
effort = 0
print("Cells:")

for i in range(len(fire)):
    current_fire_level = fire[i].split()
    fire_level = int(current_fire_level[2])
    if water < fire_level:
        continue

    if current_fire_level[0] == "High":
        if 81 <= fire_level <= 125:
            water -= fire_level
            total_fire += fire_level
            effort += fire_level * 0.25
            print("- " + str(fire_level))
    elif current_fire_level[0] == "Medium":
        if 51 <= fire_level <= 80:
            water -= fire_level
            total_fire += fire_level
            effort += fire_level * 0.25
            print("- " + str(fire_level))
    elif current_fire_level[0] == "Low":
        if 1 <= fire_level <= 50:
            water -= fire_level
            total_fire += fire_level
            effort += fire_level * 0.25
            print("- " + str(fire_level))

# Print Output

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
