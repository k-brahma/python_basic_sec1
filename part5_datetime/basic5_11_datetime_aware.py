"""
aware な日付時刻を生成するには、 tzinfo を指定します。
"""

from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime(2022, 7, 1, 13, 15, 0, tzinfo=ZoneInfo("Asia/Tokyo"))
print(dt)

print(type(dt))
print(dt)

print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second, dt.microsecond)

# naive な日付時刻は、 tzinfo を有します
print(dt.tzinfo)
print(dt.utcoffset())
