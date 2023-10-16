#Read User Input
num1, num2 = int(input()), int(input())

#Logic

string = ""

for i in range(num1, num2 + 1):
    if i == num2:
        string += chr(i)
    else:
        string += chr(i) + " "

#Print Output

print(string)