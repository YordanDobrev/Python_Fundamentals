#Read User Input
quantity = int(input())
days = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

#Logic
total_cost = 0
total_spirit = 0

for i in range(1,days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total_cost += quantity * ornament_set_price
        total_spirit += 5
    if i % 3 == 0:
        total_cost += quantity * (tree_skirt_price + tree_garland_price)
        total_spirit += 3 + 10
    if i % 5 == 0:
        total_cost += quantity * tree_lights_price
        total_spirit += 17
        if i % 3 == 0:
            total_spirit += 30
    if i % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt_price + tree_garland_price + tree_lights_price

if days % 10 == 0:
    total_spirit -= 30

#Print Output

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")