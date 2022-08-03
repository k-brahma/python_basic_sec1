"""
datetime.datetime は 日付時刻 のオブジェクトでした。
datetime.date     は 日付    のオブジェクトです。

date には、timezone の概念はありません。
"""
from datetime import datetime, timedelta

today = datetime.now().date()
print(type(today))
print(today)

tomorrow = today + timedelta(days=1)
print(tomorrow)

# 時刻の情報は持たないので、以下の演算は無効です
today_three_am = today + timedelta(hours=3)
print(today_three_am)
