message = input()
encrypted_text = ""

for index in range(len(message)):
    encrypted_text += chr(ord(message[index]) + 3)

print(encrypted_text)