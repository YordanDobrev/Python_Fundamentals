file_path = input().split(".")

file_name = file_path[0].split("\\")
file_extension = file_path[1]

print(f"File name: {file_name[-1]}")
print(f"File extension: {file_extension}")