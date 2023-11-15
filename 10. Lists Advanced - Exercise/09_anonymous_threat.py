# line = input().split()
# new_list = []
# command = input()
#
# while command != "3:1":
#     current_command = command.split()
#     action = current_command[0]
#     start_index = int(current_command[1])
#     end_index = int(current_command[2])
#     new_word = ""
#
#     if action == "merge":
#         if start_index < 0:
#             start_index = 0
#         if end_index > len(line) - 1:
#             end_index = len(line) - 1
#         merged_elements = "".join(line[start_index:end_index + 1])
#
#         line[start_index:end_index + 1] = merged_elements
#
#     elif action == "devide":
#         element = line[start_index]
#         divided_partition = []
#         partition_length = len(element) // end_index
#         for current_element in range(end_index):
#             divided_partition.append(element[current_element])
#         line[start_index:start_index + 1] = divided_partition
#
#     command = input()
#
# print(new_list)
