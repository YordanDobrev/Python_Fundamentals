import re

letters_to_search = ["s", "t", "a", "r"]
new_words = []
lines = int(input())

for index in range(lines):
    current_line = input()
    star_count = 0
    word_to_append = ""

    for line in range(len(current_line)):
        if current_line[line].lower() in letters_to_search:
            star_count += 1

    for char in range(len(current_line)):
        current_word = current_line[char]
        decrypted_word = ord(current_word) - star_count
        word_to_append += chr(decrypted_word)

    new_words.append(word_to_append)

# ------------------------- READY -------------------------------

pattern = r"@([a-zA-Z]+)[^@\-!:>]*:([0-9]+)[^@\-!:>]*!([AD])![^@\-!:>]*->([0-9]+)"
destroyed_planets = []
attacked_planets = []

for planet in new_words:
    match = re.finditer(pattern, planet)
    for i in match:
        planet_name = i.group(1)
        planet_population = i.group(2)
        attack_type = i.group(3)
        planet_soldiers = i.group(4)
        if attack_type == "D":
            destroyed_planets.append(planet_name)
        else:
            attacked_planets.append(planet_name)

# ------------------------- READY -------------------------------

att_sort = sorted(attacked_planets)
destroyed_sort = sorted(destroyed_planets)

print(f"Attacked planets: {len(attacked_planets)}")
for attack in att_sort:
    print(f"-> {attack}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for destroy in destroyed_sort:
    print(f"-> {destroy}")
