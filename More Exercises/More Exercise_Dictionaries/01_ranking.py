pass_for_contest = {}
contest = {}

pass_command = input()
while pass_command != "end of contests":
    current_pass = pass_command.split(":")
    pass_for_contest[current_pass[0]] = current_pass[1]
    pass_command = input()

contest_command = input()
while contest_command != "end of submissions":
    current_contest = contest_command.split("=>")

    if current_contest[0] in pass_for_contest.keys() and current_contest[1] in pass_for_contest.values():
        if current_contest[2] in contest.keys():
            contest[current_contest[2]].append(current_contest[0])
            contest[current_contest[2]].append(current_contest[3])
        else:
            contest[current_contest[2]] = [current_contest[0], current_contest[3]]

    contest_command = input()

total_points = 0

for key, values in sorted(contest.items()):
    tanq_dict = {}
    print(key)
    for i in range(0, len(values), 2):
        course = values[i]
        score = int(values[i + 1])
        if course not in tanq_dict.keys():
            tanq_dict[course] = score
        if score > tanq_dict[course]:
            tanq_dict[course] = score

    sorting = {k: v for k, v in sorted(tanq_dict.items(), key=lambda item: item[1])}

    for k, v in reversed(list(sorting.items())):
        print(f"#  {k} -> {v}")

# print(contest)
