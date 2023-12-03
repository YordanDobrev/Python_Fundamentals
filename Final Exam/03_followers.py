jane_facebook = {}

command = input()

while command != "Log out":
    current_command = command.split(": ")
    action = current_command[0]
    username = current_command[1]

    if action == "New follower":
        if username not in jane_facebook.keys():
            jane_facebook[username] = {"likes": 0, "comments": 0}

    elif action == "Like":
        count = int(current_command[2])
        if username not in jane_facebook.keys():
            jane_facebook[username] = {"likes": 0, "comments": 0}
        jane_facebook[username]["likes"] += count

    elif action == "Comment":
        if username not in jane_facebook.keys():
            jane_facebook[username] = {"likes": 0, "comments": 0}
        jane_facebook[username]["comments"] += 1

    elif action == "Blocked":
        if username not in jane_facebook.keys():
            print(f"{username} doesn't exist.")
        else:
            del jane_facebook[username]

    command = input()

if len(jane_facebook) > 0:
    print(f"{len(jane_facebook)} followers")

    for key, value in jane_facebook.items():
        likes_and_comments = value["likes"] + value["comments"]
        print(f"{key}: {likes_and_comments}")
