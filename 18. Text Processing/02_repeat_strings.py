line = input().split()
to_print = ""

for text in line:
    length = len(text)
    to_print += text * length

print(to_print)