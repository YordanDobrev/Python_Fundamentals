#Read User Input
num = int(input())

#Logic

for i in range(0, num):
    for j in range(0, num):
        for k in range(0, num):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")

#Print Output