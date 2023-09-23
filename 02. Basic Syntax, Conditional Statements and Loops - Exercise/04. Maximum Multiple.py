#Read User Input
divisor = int(input())
boundary = int(input())


#Logic

for i in range(boundary, divisor - 1, -1):
    if i % divisor == 0:
        print(i)
        break

#Print Output