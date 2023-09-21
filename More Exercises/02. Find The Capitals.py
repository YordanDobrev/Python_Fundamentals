#Read User Input
string = input()
my_list = []

#Logic

for i in range(len(string)):
    text = ord(string[i])
    if 65 <= ord(string[i]) <= 90:
        my_list.insert(0, i)

#Print Output

print(sorted(my_list, reverse=False))
