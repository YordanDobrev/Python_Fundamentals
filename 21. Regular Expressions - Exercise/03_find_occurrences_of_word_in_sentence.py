import re

sentence = input()
searched_word = input()

pattern = fr"\b{searched_word}\b"
match = re.findall(pattern, sentence, re.I)

print(len(match))