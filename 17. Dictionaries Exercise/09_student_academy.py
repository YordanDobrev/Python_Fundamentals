academy = {}
students = int(input())

for i in range(students):
    name = input()
    grade = float(input())

    if name not in academy.keys():
        academy[name] = []
    academy[name].append(grade)

for student, score in academy.items():
    average = sum(score) / len(score)
    if average >= 4.50:
        print(f"{student} -> {average:.2f}")
