"""
プログラム実行時の現在の日付時刻を取得します。
ただし、 timezone を気にしない (naive な)　日付時刻です。
"""
from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime.now(ZoneInfo('Asia/Tokyo'))

print(type(dt))
print(dt)

print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second, dt.microsecond)

# aware な日付時刻は、 tzinfo を有します
print(dt.tzinfo)
print(dt.utcoffset())
