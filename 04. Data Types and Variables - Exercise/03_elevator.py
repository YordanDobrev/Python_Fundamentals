#Read User Input
peoples = int(input())
capacity = int(input())

#Logic

courses = 0

while True:
    if peoples <= 0:
        break
    peoples -= capacity
    courses += 1

#Print Output

print(courses)