
def age_calculator(age):
    if age<13:
        return "Child"
    elif age >=13 and age<20:
        return "Teenager"
    elif age>=20 and age<59:
        return "Adult"
    else:
        return "Seneior Citizen"

age_category = age_calculator(0)
print(f"The person is categorized as: {age_category}")