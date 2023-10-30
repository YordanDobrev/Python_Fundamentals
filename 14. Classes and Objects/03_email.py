class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


information = []

info = input()

while info != "Stop":
    send, receive, cont = info.split()
    mail_info = Email(send, receive, cont)
    information.append(mail_info)
    info = input()

indices = [int(index) for index in input().split(", ")]

for i in indices:
    information[i].send()

for email in information:
    print(email.get_info())
