"""
naive な日付時刻同士に所定の日数、時刻等を加算します
"""
from datetime import datetime, timedelta

dt = datetime(2022, 8, 1, 13, 15, 0)
print(dt)

new_dt = dt + timedelta(days=2)
print(new_dt)

new_dt = dt + timedelta(days=-2)
print(new_dt)

new_dt = dt + timedelta(hours=3)
print(new_dt)

new_dt = dt + timedelta(hours=13)
print(new_dt)
