import re

hidden_words = input()
mirror_words = []
pattern = r"([@#])([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1"
match = re.findall(pattern, hidden_words)

for words in match:
    pair_one = words[1]
    pair_two = words[3]
    if pair_one == pair_two[::-1]:
        mirror_words.append(F"{pair_one} <=> {pair_two}")

if len(match) > 0:
    print(f"{len(match)} word pairs found!")

    if not mirror_words:
        print("No mirror words!")
    else:
        print(f"The mirror words are:\n"
              f"{', '.join(mirror_words)}")
else:
    print("No word pairs found!")
    print("No mirror words!")