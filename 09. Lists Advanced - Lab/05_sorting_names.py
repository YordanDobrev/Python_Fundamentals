# Read User Input
string = input().split(", ")

# Logic

the_list = sorted(string, key=lambda x: (-len(x), x))

# Print Output

print(the_list)
