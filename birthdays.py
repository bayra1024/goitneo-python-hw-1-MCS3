"""HW8"""
from datetime import datetime


users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
         {"name": "Galyna Tsvigun", "birthday": datetime(1989, 10, 19)},
         {"name": "Mick Kemp", "birthday": datetime(1965, 9, 11)},
         {"name": "Olena Ivanova", "birthday": datetime(1990, 10, 15)},
         {"name": "Yaromyr Shevchenko", "birthday": datetime(1999, 10, 16)}]


def get_birthdays_per_week(users):
    week_days = {"Monday": [], "Tuersday": [], "Wednesday": [], 'Thursday': [],
                 "Friday": []}
    today = datetime.today().date()
    print(f"today {today}")

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо до типу date
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        print(f"name {name} birthday {birthday_this_year}")
        delta_days = (birthday_this_year - today).days
        print(f"days before birthday {delta_days}")

        if delta_days < 7:
            weekday = birthday_this_year.weekday()
            print(weekday)
            if weekday in [0, 5, 6]:
                week_days["Monday"].append(name)
            elif weekday == 1:
                week_days["Tuersday"].append(name)
            elif weekday == 2:
                week_days["Wednesday"].append(name)
            elif weekday == 3:
                week_days["Thursday"].append(name)
            elif weekday == 4:
                week_days["Friday"].append(name)

    for key, value in week_days.items():
        if value != []:
            print(f"{key}: {', '.join(value)}")


get_birthdays_per_week(users)
