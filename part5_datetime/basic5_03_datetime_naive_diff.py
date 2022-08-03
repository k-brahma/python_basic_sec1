"""
naive な日付時刻同士の差分を計算します
"""
from datetime import datetime

dt = datetime(2022, 8, 1, 13, 15, 0)
print(dt)

now = datetime.now()

interval = now - dt
print(interval)
print(interval.days, interval.seconds)

hours = interval.seconds // 60 // 60
print(hours)

minutes = interval.seconds // 60 % 60
print(minutes)

seconds = interval.seconds % 60
print(seconds)

print(f'{interval.days}日 {hours}時間 {minutes}分 {seconds}.{interval.microseconds}秒離れています')

print('finished')
