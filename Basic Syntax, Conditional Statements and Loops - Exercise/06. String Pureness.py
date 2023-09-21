#Read User Input
string = int(input())

#Logic

for i in range(string):
    concurrent_string = input()
    if "," in concurrent_string or \
        "." in concurrent_string or \
        "_" in concurrent_string:
        print(f"{concurrent_string} is not pure!")
    else:
        print(f"{concurrent_string} is pure.")

#Print Output