# force = {}
#
# command = input()
#
# while command != "Lumpawaroo":
#
#     if " | " in command:
#         side, name = command.split(" | ")
#         part_of_the_side = False
#
#         for value in force.values():
#             if name in value:
#                 part_of_the_side = True
#                 break
#         if not part_of_the_side:
#
#
#         if side not in force.keys() and name not in force.values():
#             force[side] = []
#             force[side].append(name)
#         elif name in force.values():
#             continue
#
#     elif " -> " in command:
#         command = command.split(" -> ")
#         # side = command[0]
#         # user = command[1]
#         #
#         # if user in force.values():
#         #     force.pop(user)
#         #     force[side].append(user)
#         # elif user not in force.values():
#         #     force[side].append(user)
#         # elif user not in force.values() and side not in force.keys():
#         #     force[side].append(user)
#
#     command = input()
#
# print(force)