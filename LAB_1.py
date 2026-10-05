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



# LAB TASK 4
name = input("Enter passenger name: ")
destination = input("Enter destination: ")
tickets = int(input("Enter number of tickets: "))
passenger_type = input("Enter passenger type: ")

if destination.lower() == "dhaka":
    fare = 500
elif destination.lower() == "chittagong":
    fare = 800
elif destination.lower() == "sylhet":
    fare = 700
else:
    fare = 0
    print("Invalid destination!")

if passenger_type.lower() == "child":
    discount = 50
elif passenger_type.lower() == "student":
    discount = 20
elif passenger_type.lower() == "senior":
    discount = 15
elif passenger_type.lower() == "adult":
    discount = 0
else:
    discount = 0
    print("Invalid passenger type!")

discount_amount = fare * discount / 100
price_after_discount = fare - discount_amount
total_fare = price_after_discount * tickets


print("Passenger Name:", name)
print("Destination:", destination)
print("Passenger Type:", passenger_type)
print("Number of Tickets:", tickets)
print("Fare per Ticket:", fare)
print("Discount:", discount, "%")
print("Total Fare:", total_fare)
