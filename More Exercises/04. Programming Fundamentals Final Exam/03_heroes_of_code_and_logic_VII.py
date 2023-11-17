num_heroes = int(input())
heroes = {}
for index in range(num_heroes):
    current_hero = input().split()
    hero_name = current_hero[0]
    hero_health = int(current_hero[1])
    hero_mana = int(current_hero[2])
    heroes[hero_name] = [hero_health, hero_mana]

command = input()

while command != "End":
    current_command = command.split(" - ")
    action = current_command[0]
    hero = current_command[1]

    if action == "CastSpell":
        mana = int(current_command[2])
        spell = current_command[3]
        for key, value in heroes.items():
            current_hero_mp = value[1]
            if hero == key:
                if mana > current_hero_mp:
                    print(f"{hero} does not have enough MP to cast {spell}!")
                    break
                current_hero_mp -= mana
                heroes[hero] = [value[0], current_hero_mp]
                print(f"{hero} has successfully cast {spell} and now has {current_hero_mp} MP!")

    elif action == "TakeDamage":
        damage = int(current_command[2])
        attacker = current_command[3]
        for key, value in heroes.items():
            current_hero_hp = value[0]
            if hero == key:
                if damage >= current_hero_hp:
                    print(f"{hero} has been killed by {attacker}!")
                    del heroes[hero]
                    break
                current_hero_hp -= damage
                heroes[hero] = [current_hero_hp, value[1]]
                print(f"{hero} was hit for {damage} HP by {attacker} and now has {current_hero_hp} HP left!")

    elif action == "Recharge":
        mana_to_recharge = int(current_command[2])
        for key, value in heroes.items():
            hero_mana = value[1]
            recharged = 0
            if hero == key:
                temp_mana = hero_mana
                if mana_to_recharge + hero_mana > 200:
                    recharged = 200 - hero_mana
                    heroes[hero] = [value[0], 200]

                else:
                    recharged_mana = mana_to_recharge + hero_mana
                    recharged = mana_to_recharge
                    heroes[hero] = [value[0], recharged_mana]
                print(f"{hero} recharged for {recharged} MP!")

    elif action == "Heal":
        health_to_heal = int(current_command[2])
        for key, value in heroes.items():
            hero_hp = value[0]
            healed = 0
            if hero == key:
                if health_to_heal + hero_hp > 100:
                    healed = 100 - hero_hp
                    heroes[hero] = [100, value[1]]

                else:
                    heal = health_to_heal + hero_hp
                    healed = health_to_heal
                    heroes[hero] = [heal, value[1]]
                print(f"{hero} healed for {healed} HP!")

    command = input()

for key, value in heroes.items():
    print(key)
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")
