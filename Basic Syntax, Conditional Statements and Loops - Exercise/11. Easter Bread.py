#Read User Input
budget = float(input())
flour_price_per_kg = float(input())
eggs_price = flour_price_per_kg * 0.75
milk_price = flour_price_per_kg * 1.25

#Logic

bread = 0
coloured_eggs = 0

while budget >= 0:
    if flour_price_per_kg + eggs_price + (milk_price/4) > budget:
        break
    else:
        budget -= flour_price_per_kg + eggs_price + (milk_price/4)
        bread += 1
        coloured_eggs += 3
    if bread % 3 == 0:
        coloured_eggs -= bread - 2

#Print Output

print(f"You made {bread} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")
