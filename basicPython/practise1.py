from datetime import datetime

my_name = "Preeti Sharma"
my_age = 27
favorite_hobby = "Coding"
single_sentence = f"My name is {my_name}, I'm {my_age} years old, and I love {favorite_hobby}"
print(single_sentence)


num1 = 10
num2 = 8
sum = num1+num2
difference = num1-num2
product = num1*num2
division = num1/num2
print(sum, difference, product, division)

user_dob = "05-08-2025"
dob = datetime.strptime(user_dob, "%d-%m-%Y")

# calculating year, date and months
current_date = datetime.now()
# Initial difference from curr date
year = current_date.year - dob.year
month = current_date.month - dob.month
days = current_date.day - dob.day

# Adjust days if negative
if days < 0:

    previous_month = current_date.month - 1 if current_date.month > 1 else 12
    previous_year = current_date.year if current_date.month > 1 else current_date.year - 1
    days_in_prev_month = (datetime(previous_year, previous_month + 1,
                          1) - datetime(previous_year, previous_month, 1)).days
    days += days_in_prev_month
    month -= 1

if month < 0:
    month += 12
    year -= 1

print(f"{year} years {month} months {days} days")
