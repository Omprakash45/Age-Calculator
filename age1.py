from datetime import datetime

class Age:
    def __init__(self, years, month, day):
        self.years = years
        self.month = month
        self.day = day

    @staticmethod
    def user_age():
        user_year = int(input("Enter your year of birth: ->"))
        if len(str(user_year)) != 4:
            print("Please enter a valid year (4 digits).")
            return

        user_month = int(input("Enter your month of birth: ->"))
        if not 1 <= user_month <= 12:
            print("Please enter a valid month (1-12).")
            return

        user_day = int(input("Enter your day of birth: ->"))
        if not 1 <= user_day <= 31:
            print("Please enter a valid day (1-31).")
            return

        today = datetime.now()
        # Calculate age
        age = today.year - user_year - ((today.month, today.day) < (user_month, user_day))
        months = today.month - user_month - (today.day < user_day)
        days = today.day - user_day
        if months < 0:
            age -= 1
            months += 12
        if days < 0:
            months -= 1
            days += 30

        total_days = (age * 365) + (months * 31) + days
        total_hours = total_days * 24
        total_seconds = total_hours * 3600

        return age, months, days, total_days, total_hours, total_seconds

# Example usage
age, months, days, total_days, total_hours, total_seconds = Age.user_age()
print("You are {} years, {} months, and {} days old.".format(age, months, days))
print("You are {} days, {} hours, and {} seconds old.".format(total_days, total_hours, total_seconds))