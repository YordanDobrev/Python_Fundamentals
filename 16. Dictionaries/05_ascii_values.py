ascii = {}

line = input().split(", ")

for i in range(len(line)):
    ascii[line[i]] = ord(line[i])

print(ascii)