"""
datetime.datetime は 日付時刻 のオブジェクトでした。
datetime.date     は 日付    のオブジェクトでした。
datetime.time     は 時刻    のオブジェクトです。

time には、timezone の概念があります

datetime, date と比べて利用シーンはかなり少ないです。
"""
from datetime import datetime, timedelta

now_time = datetime.now().time()
print(type(now_time))
print(now_time)

# 時刻の加算はそのままではできません
# today_three_am = now_time + timedelta(hours=3)
# print(today_three_am)

# いったん、日付時刻に変換します。それからtimedelta。その後、改めて time() で時刻だけを取り出します
temp_datetime = datetime.combine(datetime.today(), now_time)
new_datetime = temp_datetime + timedelta(hours=3)

new_time = new_datetime.time()
print(new_time)
