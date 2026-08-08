import math
def password_crack_time():
    password = input("Enter a password: ")
    spc = "!@#$%^&*()-_=+[]{}|;:',.<>/?\\"
    length = len(password)
    char_size=0

    got_upper= any(ch.isupper()for ch in password)
    got_lower= any(ch.islower()for ch in password)
    got_digits= any(ch.isdigit()for ch in password)
    got_specials = any(ch in spc for ch in password)
    
    if got_upper:
        char_size= +26
    if got_lower:
        char_size= +26
    if got_digits:
        char_size= +10
    if got_specials:
        char_size+= len(spc)
        
    
    combinations= math.pow(char_size,length)
    Guesses_per_second = 1000000000
    seconds= combinations/Guesses_per_second

    print("Total number of combinations = ",combinations)
    print("Length of the password = ",length)
    print("Estimated time to crack your password: ")
    display_time(seconds)

def display_time(seconds):
    minute = 60
    hour = 3600
    day = 86400
    month = 86400*30
    year = month*12
    
    if seconds<1:
        print(f"Password carcked instantaneously")
    elif seconds<hour:
        print(f"Password cracked in,{seconds/minute:.2f},minutes")
    elif seconds<day:
        print(f"Password cracked in,{seconds/hour:.2f},hours")
    elif seconds<month:
        print(f"Password cracked in,{seconds/day:.2f},days")
    elif seconds<year:
        print(f"Password cracked in,{seconds/month:.2f},months")
    else:
        years = seconds/year
        if years> 1000000000:
            print(f"{years:.2f}years")
            print("Password effectively UNCRACKABLE")
        else:
            print(f"{years:.2f}years")



