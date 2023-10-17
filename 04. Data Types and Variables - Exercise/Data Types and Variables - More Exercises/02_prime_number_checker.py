# Read User Input
num = int(input())

# Logic
prime = 0

for i in range(2, num):
    if num % i == 0:
        prime += 1

# Print Output
if prime == 0:
    print(True)
else:
    print(False)