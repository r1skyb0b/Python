from datetime import datetime, timedelta
import pytz
import re
import time

# Exercise 1: Age Calculator
def age_calculator():
    print("\n=== Age Calculator ===")
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        today = datetime.now()
        
        years = today.year - birthdate.year
        months = today.month - birthdate.month
        days = today.day - birthdate.day
        
        if days < 0:
            months -= 1
            prev_month = today.month - 1 if today.month > 1 else 12
            prev_month_year = today.year if today.month > 1 else today.year - 1
            days_in_prev_month = (datetime(prev_month_year, prev_month + 1, 1) - timedelta(days=1)).day if prev_month < 12 else 31
            days += days_in_prev_month
        
        if months < 0:
            years -= 1
            months += 12
        
        print(f"Your age is: {years} years, {months} months, and {days} days")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD")

# Exercise 2: Days Until Next Birthday
def days_until_birthday():
    print("\n=== Days Until Next Birthday ===")
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        today = datetime.now()
        
        next_birthday = datetime(today.year, birthdate.month, birthdate.day)
        if next_birthday < today:
            next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day)
        
        days_remaining = (next_birthday - today).days
        print(f"Days until your next birthday: {days_remaining} days")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD")

# Exercise 3: Meeting Scheduler
def meeting_scheduler():
    print("\n=== Meeting Scheduler ===")
    datetime_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
    duration_str = input("Enter meeting duration (HH:MM): ")
    try:
        current_time = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        hours, minutes = map(int, duration_str.split(":"))
        
        end_time = current_time + timedelta(hours=hours, minutes=minutes)
        print(f"Meeting will end at: {end_time.strftime('%Y-%m-%d %H:%M')}")
    except ValueError:
        print("Invalid format. Please use the correct format.")

# Exercise 4: Timezone Converter
def timezone_converter():
    print("\n=== Timezone Converter ===")
    print("Common timezones: UTC, US/Eastern, US/Pacific, Europe/London, Asia/Tokyo, Australia/Sydney")
    datetime_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    from_tz = input("Enter your current timezone: ")
    to_tz = input("Enter target timezone: ")
    try:
        from_timezone = pytz.timezone(from_tz)
        to_timezone = pytz.timezone(to_tz)
        
        naive_dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
        localized_dt = from_timezone.localize(naive_dt)
        converted_dt = localized_dt.astimezone(to_timezone)
        
        print(f"Converted time: {converted_dt.strftime('%Y-%m-%d %H:%M %Z')}")
    except Exception as e:
        print(f"Error: {e}")

# Exercise 5: Countdown Timer
def countdown_timer():
    print("\n=== Countdown Timer ===")
    target_str = input("Enter target date and time (YYYY-MM-DD HH:MM:SS): ")
    try:
        target_time = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")
        
        print("Countdown started (Press Ctrl+C to stop)...")
        while True:
            now = datetime.now()
            remaining = target_time - now
            
            if remaining.total_seconds() <= 0:
                print("\nCountdown finished!")
                break
            
            days = remaining.days
            hours, remainder = divmod(remaining.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            
            print(f"\rTime remaining: {days}d {hours}h {minutes}m {seconds}s", end="")
            time.sleep(1)
    except ValueError:
        print("Invalid date format.")
    except KeyboardInterrupt:
        print("\nCountdown stopped.")

# Exercise 6: Email Validator
def email_validator():
    print("\n=== Email Validator ===")
    email = input("Enter an email address: ")
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(pattern, email):
        print(f"'{email}' is a valid email address.")
    else:
        print(f"'{email}' is NOT a valid email address.")

# Exercise 7: Phone Number Formatter
def phone_formatter():
    print("\n=== Phone Number Formatter ===")
    phone = input("Enter a phone number: ")
    
    digits = re.sub(r'\D', '', phone)
    
    if len(digits) == 10:
        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        print(f"Formatted phone number: {formatted}")
    elif len(digits) == 11 and digits[0] == '1':
        formatted = f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:]}"
        print(f"Formatted phone number: {formatted}")
    else:
        print("Invalid phone number. Please enter a 10-digit number.")

# Exercise 8: Password Strength Checker
def password_checker():
    print("\n=== Password Strength Checker ===")
    password = input("Enter a password: ")
    
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "digit": bool(re.search(r'\d', password)),
        "special": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    
    print("\nPassword strength analysis:")
    print(f"✓ Minimum 8 characters: {'Yes' if criteria['length'] else 'No'}")
    print(f"✓ Contains uppercase letter: {'Yes' if criteria['uppercase'] else 'No'}")
    print(f"✓ Contains lowercase letter: {'Yes' if criteria['lowercase'] else 'No'}")
    print(f"✓ Contains digit: {'Yes' if criteria['digit'] else 'No'}")
    print(f"✓ Contains special character: {'Yes' if criteria['special'] else 'No'}")
    
    strength = sum(criteria.values())
    if strength == 5:
        print("\nPassword strength: STRONG ✓")
    elif strength >= 3:
        print("\nPassword strength: MEDIUM")
    else:
        print("\nPassword strength: WEAK")

# Exercise 9: Word Finder
def word_finder():
    print("\n=== Word Finder ===")
    sample_text = """Python is a high-level programming language. Python is known for its simplicity.
Many developers love Python because Python has excellent libraries and Python community support."""
    
    print("Sample text:")
    print(sample_text)
    print()
    
    word = input("Enter a word to search: ")
    
    pattern = r'\b' + re.escape(word) + r'\b'
    matches = re.finditer(pattern, sample_text, re.IGNORECASE)
    
    positions = []
    for match in matches:
        positions.append((match.start(), match.end()))
    
    if positions:
        print(f"\nFound {len(positions)} occurrence(s) of '{word}':")
        for i, (start, end) in enumerate(positions, 1):
            line_start = sample_text.rfind('\n', 0, start) + 1
            line_end = sample_text.find('\n', end)
            if line_end == -1:
                line_end = len(sample_text)
            context = sample_text[line_start:line_end]
            print(f"{i}. Position {start}: {context.strip()}")
    else:
        print(f"No occurrences of '{word}' found.")

# Exercise 10: Date Extractor
def date_extractor():
    print("\n=== Date Extractor ===")
    text = input("Enter text to extract dates from: ")
    
    date_patterns = [
        r'\d{4}-\d{2}-\d{2}',  # YYYY-MM-DD
        r'\d{2}/\d{2}/\d{4}',  # MM/DD/YYYY or DD/MM/YYYY
        r'\d{1,2}/\d{1,2}/\d{2,4}',  # M/D/YY or MM/DD/YYYY
        r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{4}\b',  # Month DD, YYYY
        r'\b\d{1,2} (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{4}\b'  # DD Month YYYY
    ]
    
    found_dates = []
    for pattern in date_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            found_dates.append(match.group())
    
    if found_dates:
        print(f"\nFound {len(found_dates)} date(s):")
        for i, date in enumerate(found_dates, 1):
            print(f"{i}. {date}")
    else:
        print("No dates found in the text.")

# Main menu
def main():
    exercises = {
        "1": ("Age Calculator", age_calculator),
        "2": ("Days Until Next Birthday", days_until_birthday),
        "3": ("Meeting Scheduler", meeting_scheduler),
        "4": ("Timezone Converter", timezone_converter),
        "5": ("Countdown Timer", countdown_timer),
        "6": ("Email Validator", email_validator),
        "7": ("Phone Number Formatter", phone_formatter),
        "8": ("Password Strength Checker", password_checker),
        "9": ("Word Finder", word_finder),
        "10": ("Date Extractor", date_extractor)
    }
    
    while True:
        print("\n" + "="*50)
        print("PYTHON HOMEWORK - SELECT AN EXERCISE")
        print("="*50)
        for key, (name, _) in exercises.items():
            print(f"{key}. {name}")
        print("0. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (0-10): ")
        
        if choice == "0":
            print("Goodbye!")
            break
        elif choice in exercises:
            exercises[choice][1]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
