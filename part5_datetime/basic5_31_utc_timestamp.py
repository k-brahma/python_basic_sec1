"""
utctimestamp を datetime.datetime 型の日付時刻に変換する
"""
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

utc_timestamp = 1659442920

naive_dt = datetime.utcfromtimestamp(utc_timestamp)
print(naive_dt)

utc_aware_dt = naive_dt.replace(tzinfo=timezone.utc)
print(utc_aware_dt)

tokyo_aware_dt = utc_aware_dt.astimezone(tz=ZoneInfo('Asia/Tokyo'))
print(tokyo_aware_dt)

print(utc_aware_dt == tokyo_aware_dt)
