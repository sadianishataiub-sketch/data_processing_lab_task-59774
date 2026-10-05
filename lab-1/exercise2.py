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
