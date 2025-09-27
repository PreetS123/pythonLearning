def movie_ticket_pricing(age, day=""):
    price = 0
    if age < 18:
        price = 8
    elif age >= 18:
        price = 12

    if day.lower() == "wednesday":
        price -= 2

    return f"${price}"


movie_price = movie_ticket_pricing(20,"Wednesday")
print(f"The ticket price is: {movie_price}")
