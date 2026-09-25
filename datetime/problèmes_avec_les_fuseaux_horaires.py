from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

montreal_tz = ZoneInfo("America/Montreal")
march_7 = datetime(2020, 3, 7, 13, 0, 0, tzinfo=montreal_tz)
march_8 = datetime(2020, 3, 8, 13, 0, 0, tzinfo=montreal_tz)
march_7_utc = march_7.astimezone(ZoneInfo("UTC"))
march_8_utc = march_8.astimezone(ZoneInfo("UTC"))
print(f"March 7 in Montreal: {march_7_utc} {march_7_utc.tzname()}")
print(f"March 8 in Montreal: {march_8_utc} {march_8_utc.tzname()}")