#Read User Input
given_money = input().split(", ")
beggars = int(input())

#Logic
given_money_list = []
summary_list = []

beggars_index = 0

for j in given_money:
    current_money = int(j)
    given_money_list.append(current_money)

while beggars_index < beggars:
    sum_beggars = 0
    for i in range(beggars_index, len(given_money_list), beggars):
        current_money = given_money_list[i]
        sum_beggars += current_money

    summary_list.append(sum_beggars)
    beggars_index += 1

#Print Output

print(summary_list)