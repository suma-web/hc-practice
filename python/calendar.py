import sys
import datetime

args = sys.argv
weekday_names = ["月","火","水","木","金","土","日"]
today = datetime.date.today()
current_month = today.month
current_year = today.year

def current_month_days(y, m):
    current_month_firtst = datetime.datetime(y, m, 1)
    if m == 12:
        current_month_last = datetime.datetime(y+1, 1, 1)
    else:
        current_month_last = datetime.datetime(y, m+1, 1)

    return (current_month_last - current_month_firtst).days

if len(args) == 3 and args[1] == "-m":
    try:
        new_current_month = int(args[2])
        current_month_days(2025, new_current_month)
    except ValueError:
        print(f"{args[2]} is neither a month number (1..12) nor a name")
        sys.exit(1)
    except TypeError:
        print(f"{args[2]} is not entered in the correct format")
        sys.exit(1)
    else:
        current_month = new_current_month

highlight_day = today.day if (today.year == current_year and today.month == current_month) else None

first_day = datetime.date(current_year, current_month, 1)
start_weekday = first_day.weekday()

print(f"{current_month:8}月 {current_year}")
print(" ".join(weekday_names)) 
print("   " * start_weekday, end="")

for day in range(1, current_month_days(current_year, current_month) + 1):
    if day == highlight_day:
        cell = f"[{day}]"
        print(cell, end="")
    else:
        print(f"{day:2d}", end=" ")

    if (start_weekday + day) % 7 == 0:
        print()