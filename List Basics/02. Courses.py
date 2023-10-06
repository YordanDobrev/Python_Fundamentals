#Read User Input
num_courses = int(input())

course_list = []

#Logic

for i in range(num_courses):
    current_course = input()
    course_list.append(current_course)

#Print Output

print(course_list)