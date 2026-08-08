import math

def password_crack_time():
    while True:
        password = input("Enter a password: ")
        length = len(password)

        if length < 7:
            return "Invalid password, Password must be at least 7 characters long. Please enter a better password."
        if length > 32:
            return "Invalid password, Password must not exceed 32 characters. Please enter a better password."

        spc = "!@#$%^&*()-_=+[]{}|;:',.<>/?\\"

        got_upper   = any(ch.isupper() for ch in password)
        got_lower   = any(ch.islower() for ch in password)
        got_digits  = any(ch.isdigit() for ch in password)
        got_specials = any(ch in spc for ch in password)

        if got_upper:
            char_size = 26
        else:
            char_size = 0
        if got_lower:
            char_size += 26
        if got_digits:
            char_size += 10
        if got_specials:
            char_size += len(spc)

        combinations = math.pow(char_size, length)
        guesses_per_second = 1000000000
        seconds = combinations / guesses_per_second
        rating = password_rating(password, got_upper, got_lower, got_digits, got_specials)

        if rating < 3:
            print("Rating: " + str(rating) + "/10 — Password is too weak! Please enter a stronger password.\n")
            continue

        time_result = display_time(seconds)
        result = (f"Password Length     : {length}\n"
            f"Total Combinations  : {combinations:.2e}\n"
            f"Crack Time Estimate : {time_result}\n"
            f"Password Rating     : {rating}/10")
        return result
    
def display_time(seconds):
    minute = 60
    hour = 3600
    day = 86400
    month = 86400 * 30
    year = month * 12

    if seconds < 1:
        return "Cracked instantaneously"
    elif seconds < hour:
        return f"Cracked in {seconds / minute:.2f} minutes"
    elif seconds < day:
        return f"Cracked in {seconds / hour:.2f} hours"
    elif seconds < month:
        return f"Cracked in {seconds / day:.2f} days"
    elif seconds < year:
        return f"Cracked in {seconds / month:.2f} months"
    else:
        years = seconds / year
        if years > 1000000000:
            return f"{years:.2f} years\nPassword is effectively uncrackable!"
        else:
            return f"{years:.2f} years"
        

def password_rating(password, got_upper, got_lower, got_digits, got_specials):
    rating = 0

    length = len(password)
    if length >= 8:
        rating += 1
    if length >= 12:
        rating += 1
    if length >= 16:
        rating += 1
    if length >= 20:
        rating += 1
    if got_upper:
        rating += 1
    if got_lower:
        rating += 1
    if got_digits:
        rating += 1
    if got_specials:
        rating += 1
    if got_upper and got_lower and got_digits and got_specials:
        rating += 1
    if length >= 16 and got_upper and got_lower and got_digits and got_specials:
        rating += 1
    if rating > 10:
        rating = 10
    return rating    

print(password_crack_time())