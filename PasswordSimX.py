import random
def password_crack_time():
    while True:
        try:
            gate = int(input("Press 1 to Enter, 0 to Exit: "))
        except ValueError:
            print("Please enter only 0 or 1.")
            continue
        if gate==0:
           print("Thank you for using Our PasswordSim") 
           break
        elif gate>1:
            print("0 or 1 only please")
            continue

        password = input("Enter a password: ")
        length = len(password)
        
        if length < 7:
            print("❌ Password must be at least 7 characters long. Try again.\n")
            continue
        if length > 32:
            print("❌ Password must not exceed 32 characters. Try again.\n")
            continue

        spc = "!@#$%^&*()-_=+[]{}|;:',.<>/?\\"

        got_upper    = any(ch.isupper() for ch in password)
        got_lower    = any(ch.islower() for ch in password)
        got_digits   = any(ch.isdigit() for ch in password)
        got_specials = any(ch in spc for ch in password)

        char_size = 0
        if got_upper:    char_size += 26
        if got_lower:    char_size += 26
        if got_digits:   char_size += 10
        if got_specials: char_size += len(spc)

        if char_size == 0:
            char_size = 1 

        combinations = char_size**length
        guesses_per_second = 1000000000
        seconds = combinations / guesses_per_second
        rating,reasons = password_rating(password, got_upper, got_lower, got_digits, got_specials)
        funny_message = common_password_check(password)
        if rating < 3:
            print(f"Rating: {rating}/10 — Password is too weak! Please enter a stronger password.\n")
            print(funny_message)
            continue

        time_result = display_time(seconds)
        print("\n" + "="*100)
        print(f"Password Length     : {length}")
        print(f"Character Pool Size : {char_size}")
        print(f"Total Combinations  : {combinations:.2e}")
        print(f"Crack Time Estimate : {time_result}")
        print(f"Password Rating     : {rating}/10")

        print("\nStrength Breakdown")
        for reason in reasons:
            print(reason)

        print(f"\nFinal Score: {rating}/10")
        print("="*100)

        if rating < 6:
            suggestions = get_suggestions(length, got_upper, got_lower, got_digits, got_specials)
            if suggestions:
                print("\n💡 Tips to boost your score to 9 or 10:")
                for tip in suggestions:
                    print(f" - {tip}")
    
def display_time(seconds):

    minute = 60
    hour = 3600
    day = 86400
    year = 31536000

    years = int(seconds // year)
    seconds %= year

    days = int(seconds // day)
    seconds %= day

    hours = int(seconds // hour)
    seconds %= hour

    minutes = int(seconds // minute)
    seconds %= minute

    seconds = int(seconds)

    time_parts = []

    if years:

        readable_years = large_number_name(years)
        scientific = f"{years:.2e}"

        time_parts.append(
            f"{readable_years} years ({scientific})"
        )
    if days:
        time_parts.append(
            f"{days} day{'s' if days != 1 else ''}"
        )
    if hours:
        time_parts.append(
            f"{hours} hour{'s' if hours != 1 else ''}"
        )
    if minutes:
        time_parts.append(
            f"{minutes} minute{'s' if minutes != 1 else ''}"
        )
    if seconds:
        time_parts.append(
            f"{seconds} second{'s' if seconds != 1 else ''}"
        )
    if not time_parts:
        return "Instantly (<1 second)"

    return ", ".join(time_parts)
        

def password_rating(password, got_upper, got_lower, got_digits, got_specials):
    rating = 0
    reasons = []

    length = len(password)

    if length >= 8:
        rating += 1
        reasons.append("🟢 +1 Length ≥ 8")

    if length >= 12:
        rating += 1
        reasons.append("🟢 +1 Length ≥ 12")

    if length >= 16:
        rating += 1
        reasons.append("🟢 +1 Length ≥ 16")

    if length >= 20:
        rating += 1
        reasons.append("🟢 +1 Length ≥ 20")

    if got_upper:
        rating += 1
        reasons.append("🟢 +1 Uppercase letters")

    if got_lower:
        rating += 1
        reasons.append("🟢 +1 Lowercase letters")

    if got_digits:
        rating += 1
        reasons.append("🟢 +1 Numbers")

    if got_specials:
        rating += 1
        reasons.append("🟢 +1 Special characters")

    if got_upper and got_lower and got_digits and got_specials:
        rating += 1
        reasons.append("🟢 +1 Variety bonus")

    if length >= 16 and got_upper and got_lower and got_digits and got_specials:
        rating += 1
        reasons.append("🟢 +1 Elite security bonus")

    weak_patterns = ["123", "password", "admin", "qwerty", "abc", "000"]

    lowered = password.lower()

    for pattern in weak_patterns:
        if pattern in lowered:
            rating -= 2
            reasons.append(f"🔴 -2 Contains '{pattern}'")

    rating = max(0, min(rating, 10))

    return rating, reasons
def get_suggestions(length, got_upper, got_lower, got_digits, got_specials):
    suggestions = []
    has_everything = got_upper and got_lower and got_digits and got_specials
    if has_everything and length < 12:
        suggestions.append(f" Your complexity is perfect, but your password is too short ({length} characters)!")
        suggestions.append("   Even complex passwords can be brute-forced quickly if they are short💔🥀.")
        suggestions.append("   Add more characters (aim for 14-16+) to dramatically increase crack time📈.")
        return suggestions 
    

    if length < 14:
        suggestions.append(f"Make it longer! Your current length is {length}. Increasing it past 14-16 characters multiplies safety exponentially.")
    
    if not got_upper:    suggestions.append("Add at least one uppercase letter (A-Z).")
    if not got_lower:    suggestions.append("Add at least one lowercase letter (a-z).")
    if not got_digits:   suggestions.append("Include numbers (0-9).")
    if not got_specials: suggestions.append("Mix in special characters like (@, #, $, %, etc.).")
        
    if not has_everything:
        suggestions.append("Unlock a variety bonus point by combining all 4 character types.")
        
    return suggestions

def large_number_name(number):
    names = ["", "thousand", "million", "billion",
        "trillion", "quadrillion", "quintillion",
        "sextillion", "septillion", "octillion",
        "nonillion", "decillion", "undecillion",
        "duodecillion", "tredecillion",
        "quattuordecillion", "quindecillion",
        "sexdecillion", "septendecillion",
        "octodecillion", "novemdecillion",
        "vigintillion"]
    

    if number >= 10**1000:
        return "googolplex"
    if number >= 10**100:
        return "googol"
    group = 0
    temp = float(number)

    while temp >= 1000 and group < len(names) - 1:
        temp /= 1000
        group += 1
        

    return f"{temp:.2f} {names[group]}"

def common_password_check(password):
    lowered = password.lower()

    jokes = {
    "common": ["Bro chose the tutorial password.",
               "A hacker guessed this before you finished typing it.",
               "Cybersecurity is crying in the corner right now.",
               "Even my calculator predicted this password.",
               "Another computer in the wrong hands 🥀"],

    "repeat": ["Repeating the same character? Bold strategy.",
               "Ctrl+C Ctrl+V ahh password.",
               "Your creativity has left the server.",
               "I have seen more variety in a brick wall."],

    "numbers": ["Only numbers? What is this, a phone number?",
                "Bro protecting his account with math homework.",
                "This password belongs in a calculator.",
                "The bank PIN starter pack."],

    "lowercase": ["Capital letters are apparently too expensive.",
                  "Your Shift key feels abandoned.",
                  "This password has the energy of plain toast.",
                  "Lowercase-only detected. Security level: sleepy."],

    "uppercase": ["WHY ARE WE SCREAMING THE PASSWORD??",
                  "Your password sounds angry.",
                  "Bro's password is having an argument.",
                  "This password was typed with pure rage."],
    "keyboard": ["Did you just slide your hand across the keyboard?",
                 "Keyboard pattern detected. Very original.",
                 "A raccoon walking on a keyboard could guess this.",
                 "Peak laziness unlocked."],

    "password_word": ['Using "password" in your password is insane work.',
                      'You really looked at every word and chose "password".',
                      'The hackers thank you for your cooperation.'],

    "short": ["Shorter than my attention span.",
              "Blink once and it's cracked.",
              "This password is on life support.",
              "Built like a free trial."],

    "nospecial": ["Special characters are scared of you.",
                  "Your password has less variety than airplane food.",
                  "The symbol key is not just decoration."]
}
    common_passwords = {
        "123456", "password", "qwerty", "abc123",
        "admin", "iloveyou", "111111", "123123",
        "welcome", "password123", "helloworld",
        "india1947", "56781234", "spiderman"
    }
    
    
    keyboard_patterns = ("qwerty", "asdf", "zxcv")

    if lowered in common_passwords:
        return random.choice(jokes["common"])

    if len(set(password)) == 1:
        return random.choice(jokes["repeat"])
    

    if len(set(password)) == 1:
        return random.choice(jokes["repeat"])

    if password.isdigit():
        return random.choice(jokes["numbers"])

    if password.islower() and password.isalpha():
        return random.choice(jokes["lowercase"])

    if password.isupper() and password.isalpha():
        return random.choice(jokes["uppercase"])

    if any(pattern in lowered for pattern in keyboard_patterns):
        return random.choice(jokes["keyboard"])

    if "password" in lowered:
        return random.choice(jokes["password_word"])

    if len(password) < 10:
        return random.choice(jokes["short"])

    specials = "!@#$%^&*()-_=+[]{}|;:',.<>/?\\"

    if not any(ch in specials for ch in password):
        return random.choice(jokes["nospecial"])

    return "No obvious weaknesses detected."

password_crack_time()
