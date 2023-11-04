synonyms = {}
n = int(input())

for pairs in range(n):
    current_key = input()
    current_value = input()

    if current_key not in synonyms:
        synonyms[current_key] = []
    synonyms[current_key].append(current_value)

for printing in synonyms:
    print(f"{printing} - {', '.join(synonyms[printing])}")