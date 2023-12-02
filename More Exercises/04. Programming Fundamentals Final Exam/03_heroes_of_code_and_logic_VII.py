def spell(hero_name, mana_need, spell_name):
    if all_heroes[hero_name]["mana"] >= mana_need:
        all_heroes[hero_name]["mana"] -= mana_need
        return f"{hero_name} has successfully cast {spell_name} and now has {all_heroes[hero_name]['mana']} MP!"
    return f"{hero_name} does not have enough MP to cast {spell_name}!"


def damage(name_of_hero, damage_taken, attacker):
    all_heroes[name_of_hero]["health"] -= damage_taken
    hp = all_heroes[name_of_hero]["health"]
    if all_heroes[name_of_hero]["health"] > 0:
        return f"{name_of_hero} was hit for {damage_taken} HP by {attacker} and now has {hp} HP left!"
    del all_heroes[name_of_hero]
    return f"{name_of_hero} has been killed by {attacker}!"


def recharge(hero_to_recharge, recharge_mana):
    temp_mana = all_heroes[hero_to_recharge]["mana"]
    if all_heroes[hero_to_recharge]["mana"] + recharge_mana > 200:
        all_heroes[hero_to_recharge]["mana"] = 200
    else:
        all_heroes[hero_to_recharge]["mana"] += recharge_mana
    recharged_amount = all_heroes[hero_to_recharge]["mana"] - temp_mana
    return f"{hero_to_recharge} recharged for {recharged_amount} MP!"


def heal(some_hero, heal_move):
    temp_heal = all_heroes[some_hero]["health"]
    if all_heroes[some_hero]["health"] + heal_move > 100:
        all_heroes[some_hero]["health"] = 100
    else:
        all_heroes[some_hero]["health"] += heal_move
    healed_points = all_heroes[some_hero]["health"] - temp_heal
    return f"{some_hero} healed for {healed_points} HP!"


number_heroes = int(input())
all_heroes = {}

for index in range(number_heroes):
    current_hero = input().split()
    name = current_hero[0]
    health = int(current_hero[1])
    mana = int(current_hero[2])

    all_heroes[name] = {"health": health, "mana": mana}

command = input()

while command != "End":
    current_command = command.split(" - ")
    action = current_command[0]
    hero = current_command[1]

    if action == "CastSpell":
        spell_mana = int(current_command[2])
        name_of_the_spell = current_command[3]
        print(spell(hero, spell_mana, name_of_the_spell))

    elif action == "TakeDamage":
        damage_to_take = int(current_command[2])
        attacking_npc = current_command[3]
        print(damage(hero, damage_to_take, attacking_npc))

    elif action == "Recharge":
        mana_to_recharge = int(current_command[2])
        print(recharge(hero, mana_to_recharge))

    elif action == "Heal":
        heal_amount = int(current_command[2])
        print(heal(hero, heal_amount))

    command = input()

for key, value in all_heroes.items():
    print(f"{key}\n"
          f"  HP: {value['health']}\n"
          f"  MP: {value['mana']}")

# ----------------------------- FIRST VERSION --------------------------
# num_heroes = int(input())
# heroes = {}
# for index in range(num_heroes):
#     current_hero = input().split()
#     hero_name = current_hero[0]
#     hero_health = int(current_hero[1])
#     hero_mana = int(current_hero[2])
#     heroes[hero_name] = [hero_health, hero_mana]
#
# command = input()
#
# while command != "End":
#     current_command = command.split(" - ")
#     action = current_command[0]
#     hero = current_command[1]
#
#     if action == "CastSpell":
#         mana = int(current_command[2])
#         spell = current_command[3]
#         for key, value in heroes.items():
#             current_hero_mp = value[1]
#             if hero == key:
#                 if mana > current_hero_mp:
#                     print(f"{hero} does not have enough MP to cast {spell}!")
#                     break
#                 current_hero_mp -= mana
#                 heroes[hero] = [value[0], current_hero_mp]
#                 print(f"{hero} has successfully cast {spell} and now has {current_hero_mp} MP!")
#
#     elif action == "TakeDamage":
#         damage = int(current_command[2])
#         attacker = current_command[3]
#         for key, value in heroes.items():
#             current_hero_hp = value[0]
#             if hero == key:
#                 if damage >= current_hero_hp:
#                     print(f"{hero} has been killed by {attacker}!")
#                     del heroes[hero]
#                     break
#                 current_hero_hp -= damage
#                 heroes[hero] = [current_hero_hp, value[1]]
#                 print(f"{hero} was hit for {damage} HP by {attacker} and now has {current_hero_hp} HP left!")
#
#     elif action == "Recharge":
#         mana_to_recharge = int(current_command[2])
#         for key, value in heroes.items():
#             hero_mana = value[1]
#             recharged = 0
#             if hero == key:
#                 temp_mana = hero_mana
#                 if mana_to_recharge + hero_mana > 200:
#                     recharged = 200 - hero_mana
#                     heroes[hero] = [value[0], 200]
#
#                 else:
#                     recharged_mana = mana_to_recharge + hero_mana
#                     recharged = mana_to_recharge
#                     heroes[hero] = [value[0], recharged_mana]
#                 print(f"{hero} recharged for {recharged} MP!")
#
#     elif action == "Heal":
#         health_to_heal = int(current_command[2])
#         for key, value in heroes.items():
#             hero_hp = value[0]
#             healed = 0
#             if hero == key:
#                 if health_to_heal + hero_hp > 100:
#                     healed = 100 - hero_hp
#                     heroes[hero] = [100, value[1]]
#
#                 else:
#                     heal = health_to_heal + hero_hp
#                     healed = health_to_heal
#                     heroes[hero] = [heal, value[1]]
#                 print(f"{hero} healed for {healed} HP!")
#
#     command = input()
#
# for key, value in heroes.items():
#     print(key)
#     print(f"  HP: {value[0]}")
#     print(f"  MP: {value[1]}")
