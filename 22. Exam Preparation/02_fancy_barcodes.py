import re

barcodes = int(input())
pattern = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"

for codes in range(barcodes):
    line = input()
    match = re.findall(pattern, line)

    if len(match) == 0:
        print("Invalid barcode")
        continue

    digit_match = re.findall(r"\d", match[0])

    if digit_match:
        print(f'Product group: {"".join(digit_match)}')
    else:
        print(f'Product group: 00')
