print("=================================================================================================================")
print("                              RAILWAY TICKET BOOKING SYSTEM                                   ")
print("=================================================================================================================")
#passenger details
name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
train_number = input("Enter the train number: ")
#train details
train_name = input("Enter the train name: ")

#ticket details
ticket_type = input("Enter the ticket type (AC/Non-AC): ")
source = input("Enter the source station: ")
destination = input("Enter the destination station: ")
distance = float(input("Enter the distance between source and destination (in km): "))

price_per_km = 5
total_price = distance * price_per_km
print(f"Total price for the ticket: ${total_price}")
print("===============================================TRAIN TICKET==================================================================")
print(f"Passenger Name: {name}")
print(f"Age: {age}")
print(f"Gender: {gender}")
print(f"Train Number: {train_number}")
print(f"Train Name: {train_name}")
print(f"Ticket Type: {ticket_type}")
print(f"Source: {source}")
print(f"Destination: {destination}")
print(f"Distance: {distance} km")
print(f"Total Price: ${total_price}")
