
def weather_activity(weather_type):
    if weather_type == "sunny":
        return "Go for a walk."
    elif weather_type == "rainy":
        return "Have pakoda and samosa."
    elif weather_type == "snowy":
        return "Build a snowman."
    elif weather_type == "cloudy":
        return "Go for a drive."
    else:
        return "Stay indoors and read a book."

activity = weather_activity("cloudy")
print(f"Suggested activity: {activity}")
