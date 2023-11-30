targets = input().split()
command = input()
targets_shot = 0

while command != "End":
    index = int(command)

    if 0 <= index < len(targets):
        current_target = int(targets[index])
        for i in range(len(targets)):
            if targets[i] == "-1":
                continue
            elif index == i:
                targets[i] = "-1"
                targets_shot += 1
            elif int(targets[i]) > current_target:
                targets[i] = str(int(targets[i]) - current_target)
            elif int(targets[i]) <= current_target:
                targets[i] = str(int(targets[i]) + current_target)

    command = input()

print(f"Shot targets: {targets_shot} ->", ' '.join(targets))
