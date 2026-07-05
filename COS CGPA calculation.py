# Personal Pocket CGPA Calculator

print("===== PERSONAL POCKET CGPA CALCULATOR =====")

courses = int(input("Enter number of courses: "))

total_grade_points = 0
total_units = 0

for i in range(courses):
    print(f"\nCourse {i+1}")

    unit = int(input("Course Unit: "))
    score = float(input("Course Score: "))

    if score >= 70:
        grade = "A"
        point = 5
    elif score >= 60:
        grade = "B"
        point = 4
    elif score >= 50:
        grade = "C"
        point = 3
    elif score >= 45:
        grade = "D"
        point = 2
    elif score >= 40:
        grade = "E"
        point = 1
    else:
        grade = "F"
        point = 0

    print("Grade:", grade)

    total_grade_points += point * unit
    total_units += unit

cgpa = total_grade_points / total_units

print("\n===== RESULT =====")
print("Total Units:", total_units)
print("Total Grade Points:", total_grade_points)
print("CGPA =", round(cgpa, 2))

if cgpa >= 4.50:
    print("Class of Degree: First Class")
elif cgpa >= 3.50:
    print("Class of Degree: Second Class Upper")
elif cgpa >= 2.40:
    print("Class of Degree: Second Class Lower")
elif cgpa >= 1.50:
    print("Class of Degree: Third Class")
elif cgpa >= 1.00:
    print("Class of Degree: Pass")
else:
    print("Class of Degree: Fail")