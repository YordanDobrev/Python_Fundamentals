import re

num = int(input())
regex = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"

for index in range(num):
    current_barcode = input()
    match = re.findall(regex, current_barcode)
    if len(match) == 0:
        print(f"Invalid barcode")
        continue

    group = "Product group: "
    digits = ""

    for i in current_barcode:
        if i.isdigit():
            digits += i

    if digits == "":
        group += "00"
    else:
        group += digits

    print(group)
