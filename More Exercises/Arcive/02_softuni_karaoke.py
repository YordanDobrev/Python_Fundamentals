participants = []
songs = []
contest = {}

current_participants = input().split(", ")

for singer in current_participants:
    participants.append(singer)

songs_to_sing = input().split(", ")

for current_song in songs_to_sing:
    songs.append(current_song)

command = input()

while command != "dawn":
    current_command = command.split(", ")
    name = current_command[0]
    the_song = current_command[1]
    award = current_command[2]

    if name in participants and the_song in songs:
        if name not in contest.keys():
            contest[name] = []
        if award not in contest[name]:
            contest[name].append(award)
    command = input()

if len(contest) > 0:
    for key, values in sorted(contest.items(), reverse=True):
        print(f"{key}: {len(values)} awards")
        for index in values:
            print(f"--{index}")
else:
    print("No awards")
