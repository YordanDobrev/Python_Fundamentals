def happy(the_list, factor_happiness):
    new_list = []
    for i in the_list:
        new_score = int(i)*factor_happiness
        new_list.append(new_score)
        average_score = sum(new_list) // len(new_list)

    happy_people = list(filter(lambda x: int(x) > average_score,new_list))

    if len(happy_people) < len(new_list) / 2:
        return f"Score: {len(happy_people)}/{len(new_list)}. Employees are not happy!"
    else:
        return f"Score: {len(happy_people)}/{len(new_list)}. Employees are happy!"


# Read User Input
happiness_score = input().split()
factor = int(input())

# Logic


# Print Output

print(happy(happiness_score,factor))