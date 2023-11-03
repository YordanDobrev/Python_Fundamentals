def search():
    key = input().split()

    for j in key:
        if j in bakery:
            print(f"We have {bakery[j]} of {j} left")
        else:
            print(f"Sorry, we don't have {j}")


bakery = {}

line = input().split()

for i in range(0, len(line), 2):
    product = line[i]
    quantity = line[i + 1]
    bakery[product] = int(quantity)

search()
