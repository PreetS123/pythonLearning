

def password_check(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) >=6 and len(password)<=11:
        return "Medium"
    else:
        return "Strong"