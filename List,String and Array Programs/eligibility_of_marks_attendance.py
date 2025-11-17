n = int(input("Enter no. of students: "))
array = list(map(int, input("Enter marks and attendance(comma-separated): ").split(",")))
eligible_students = []

for i in range(0, len(array), 2):
    marks = array[i]
    attendance = array[i + 1]
    if marks >= 75 and attendance >= 80:
        eligible_students.append((marks, attendance))

print("Eligible students (marks,attendance):", eligible_students)
print("Total eligible students:", len(eligible_students))
