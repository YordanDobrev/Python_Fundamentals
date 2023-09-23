#Read User Input
budget = int(input())
command = input()

#Logic

while command != "End":
    current_amount = int(command)
    budget -= current_amount

    if budget < 0:
        print("You went in overdraft!")
        break
    command = input()
else:
    print("You bought everything needed.")

#Print Output
