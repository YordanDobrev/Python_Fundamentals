contest_name = {}
command = input()
individual_standing = {}

while command != "no more time":
    line = command.split(" -> ")
    name = line[0]
    contest = line[1]
    points = int(line[2])

    if contest not in contest_name.keys():
        contest_name[contest] = {}
        contest_name[contest][name] = points

    elif contest in contest_name.keys():
        if name not in contest_name[contest].values():
            contest_name[contest][name] = points

    command = input()

dict_to_print = {}

for key, values in contest_name.items():
    value_sorting = {k: v for k, v in sorted(values.items(), key=lambda item: item[1], reverse=True)}
    dict_to_print = value_sorting
    print(f"{key}: {len(values)} participants")
    rows = 0

    for name, points in value_sorting.items():
        rows += 1
        if name not in individual_standing.keys():
            individual_standing[name] = points
        else:
            individual_standing[name] += points
        print(f"{rows}. {name} <::> {points}")

individual_standing_to_print = {k: v for k, v in
                                sorted(individual_standing.items(), key=lambda item: item[1], reverse=True)}
print(f"Individual standings:")
row = 1
for individual, score in individual_standing_to_print.items():
    print(f"{row}. {individual} -> {score}")
    row += 1
