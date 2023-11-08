duel_stats = {}

command = input()

while command != "Season end":
    current_line = command.split(" -> ")
    name = current_line[0]
    skill = current_line[1]
    points = int(current_line[2])

    if name not in duel_stats.keys():
        duel_stats[name] = {skill: points}
        for i in duel_stats.values():
            for skill, points in i.items():
                print(name, skill , points)

    command = input()

