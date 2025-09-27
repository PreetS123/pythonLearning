
def grade_calculator(score):
    if score < 60:
        return "F"
    elif score >=60 and score<70:
        return "D"
    elif score>=70 and score<80:
        return "C"
    elif score>=80 and score<90:
        return "B"
    else:
        return "A"

grade = grade_calculator(85)
print(f"The grade for the score is: {grade}")