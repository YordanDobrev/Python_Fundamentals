text = input()

for index in range(len(text)):
    current_index = text[index]
    if ":" in text[index]:
        print(f":{text[index+1]}")