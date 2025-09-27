
def transport_mode(distance):
    if distance <3:
        return "walk"
    elif distance >3 and distance<=15:
        return "Bike"
    else:
        return "Car"

print(transport_mode(2))  # Output: walk
print(transport_mode(10)) # Output: Bike
print(transport_mode(20)) # Output: Car