name = input()
age = int(input())
employee_id = int(input())
salary = float(input())

padding_number = (8 - len(str(employee_id))) * "0"

print(f"Name: {name}\n"
      f"Age: {age}\n"
      f"Employee ID: {padding_number}{employee_id}\n"
      f"Salary: {salary:.2f}")
