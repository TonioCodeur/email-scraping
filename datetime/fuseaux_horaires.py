from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

paris_now = datetime.now(ZoneInfo("Europe/Paris"))

print(f"Date et heure actuelles à Paris : {paris_now.strftime('%Y-%m-%d %H:%M:%S')}")

paris_now_str = paris_now.strftime('%Y-%m-%d %H:%M:%S')

now = datetime.now(timezone.utc) + timedelta(hours=2)
print("Current UTC+2 time:", now)
print(f'Today is {now.strftime("%A, %d %B %Y")}, and the time is {now.strftime("%H:%M:%S")}')

iso = date.fromisoformat("1989-09-11")
print("Date from ISO format to my birthday:", iso)

my_birthday_str = "11 Sep 1989"
my_birthday = datetime.strptime(my_birthday_str, "%d %b %Y")

my_years_old = paris_now.year - my_birthday.year - ((paris_now.month, paris_now.day) < (my_birthday.month, my_birthday.day))
print("Number of years since my birthday:", my_years_old)
