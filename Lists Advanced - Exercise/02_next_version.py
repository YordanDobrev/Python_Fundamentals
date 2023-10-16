# Read User Input
version = input().replace(".","")

# Logic

the_new_version = int(version) + 1
the_new_list = [x for x in str(the_new_version)]

# Print Output

print(".".join(the_new_list))
