#Read User Input
lost_fight = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

#Logic

helmet_repair = lost_fight // 2
sword_repair = lost_fight // 3
shield_repair = lost_fight // (2 * 3)
armor_repair = shield_repair // 2

total_price = (helmet_price * helmet_repair) \
              + (sword_price * sword_repair) \
              + (shield_price * shield_repair) \
              + (armor_price * armor_repair)

#Print Output

print(f"Gladiator expenses: {total_price:.2f} aureus")