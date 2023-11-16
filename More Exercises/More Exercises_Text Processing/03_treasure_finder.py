def find_between(text, first, last):
    start = text.index(first) + len(first)
    end = text.index(last, start)
    return text[start:end]


sequence = input().split()
command = input()
index = 0

while command != "find":
    decrypted_message = ""
    for current_index in range(len(command)):
        if index == 4:
            index = 0
        decrypted_message += chr(ord(command[current_index]) - int(sequence[index]))
        index += 1
    index = 0
    command = input()

    type_split = find_between(decrypted_message, "&", "&")
    coordinates_split = find_between(decrypted_message, "<", ">")

    print(f"Found {type_split} at {coordinates_split}")
