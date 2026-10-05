# LAB TASK 3
student_name = input("Enter student name: ")

# inputing 5 course marks
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter mark for course {i}: "))
    marks.append(mark)

# calculating performance
total_marks = sum(marks)
average_mark = total_marks / len(marks)
highest_mark = max(marks)
lowest_mark = min(marks)

# passed courses
passed_courses = 0
for mark in marks:
    if mark >= 50:
        passed_courses += 1

if average_mark >= 80:
    performance = "Excellent"
elif average_mark >= 70:
    performance = "Good"
elif average_mark >= 60:
    performance = "Satisfactory"
elif average_mark >= 50:
    performance = "Pass"
else:
    performance = "Needs Improvement"

print("Student Name: ", student_name)
print("Total Marks: " , total_marks)
print("Average Mark: ", average_mark)
print("Highest Mark: ", highest_mark)
print("Lowest Mark: ", lowest_mark)
print("Passed Courses    : ", passed_courses)
print("Performance Class : ",performance)