
def fruit_ripness(color):
    if color == 'green':
        return "Unripe"
    elif color == "yellow":
        return "Ripe"
    elif color == "brown":
        return "Overripe"
    else:
        return "Unknown color"

fruit_status = fruit_ripness("yellow")
print(f"The fruit is: {fruit_status}")
