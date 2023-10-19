def urgent(journal, item):
    if item not in journal:
        journal.insert(0, item)
    return journal


def unnecessary(journal, item):
    if item in journal:
        journal.remove(item)
    return journal


def correct(journal, old_item, new_item):
    if old_item in journal:
        index = journal.index(old_item)
        journal[index] = new_item
    return journal


def rearrange(journal, item):
    if item in journal:
        journal.remove(item)
        journal.append(item)
    return journal


initial_list = input().split("!")

commands = input()

while commands != "Go Shopping!":
    if "Urgent" in commands:
        [command, item] = commands.split()
        initial_list = urgent(initial_list, item)
    elif "Unnecessary" in commands:
        [command, item] = commands.split()
        initial_list = unnecessary(initial_list, item)
    elif "Correct" in commands:
        [command, item1, item2] = commands.split()
        initial_list = correct(initial_list, item1, item2)
    elif "Rearrange" in commands:
        [command, item] = commands.split()
        initial_list = rearrange(initial_list, item)

    commands = input()

print(", ".join(initial_list))