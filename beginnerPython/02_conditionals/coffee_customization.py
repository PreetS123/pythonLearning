


def coffee_order(size):
    size= size.lower()
    if  size == "small":
        return "Small short"
    elif size == "medium":
        return "Medium short"
    elif size == "large":
        return "Extra shot"
    else:
        return "Extra large shot"

print(coffee_order("LARGE"))