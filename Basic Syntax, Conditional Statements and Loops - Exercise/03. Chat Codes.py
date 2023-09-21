#Read User Input
messages = int(input())

#Logic

for i in range(messages):
    current_message = int(input())
    if current_message == 88:
        print("Hello")
    elif current_message == 86:
        print("How are you?")
    elif current_message < 88:
        print("GREAT!")
    else:
        print("Bye.")

#Print Output