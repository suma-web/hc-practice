import sys
import datetime

args = sys.argv
t_w_name = ["月","火","水","木","金","土","日"]
t_m = datetime.date.today().month
t_y = datetime.date.today().year

def t_m_days(y,m):
    t_m_firtst = datetime.datetime(y,m,1)
    if m == 12:
        t_m_last = datetime.datetime(y+1,1,1)
    else:
        t_m_last = datetime.datetime(y,m+1,1)

    return (t_m_last - t_m_firtst).days

if len(args) == 3 and args[1] == "-m":
    new_t_m = int(args[2])
    try:
        t_m_days(2025, new_t_m)
    except ValueError:
        print(f"{new_t_m} is neither a month number (1..12) nor a name")
        sys.exit(1)
    else:
        t_m = new_t_m

today = datetime.date.today()
highlight_day = today.day if (today.year == t_y and today.month == t_m) else None

first_day = datetime.date(t_y, t_m, 1)
start_weekday = first_day.weekday()

print(f"{t_m:8}月 {t_y}")
print(" ".join(t_w_name)) 
print("   " * start_weekday, end="")

for day in range(1, t_m_days(t_y, t_m) + 1):
    if day == highlight_day:
        cell = f"[{day}]"
        print(cell, end="")
    else:
        print(f"{day:2d}", end=" ")

    if (start_weekday + day) % 7 == 0:
        print()