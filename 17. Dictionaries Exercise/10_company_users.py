all_companies = {}

command = input()

while command != "End":
    current_line = command.split(" -> ")
    company = current_line[0]
    employee_id = current_line[1]

    if company not in all_companies.keys():
        all_companies[company] = []
        all_companies[company].append(employee_id)
    else:
        if employee_id not in all_companies[company]:
            all_companies[company].append(employee_id)

    command = input()

for company_name, employee in all_companies.items():
    print(f"{company_name}")
    for i in range(len(employee)):
        print(f"-- {employee[i]}")
