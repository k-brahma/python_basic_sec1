"""
aware な時間、 naive な時間ともに、 datetime.datetime クラスのオブジェクトです。

datetime.replace 関数は、日付時刻の所定の部分を置き換え可能です。
tzinfo ですら変更可能です。(naive <=> aware の変更も可能)
"""
from datetime import datetime
from zoneinfo import ZoneInfo

dt = datetime(2022, 8, 1, 13, 15, 0)
print(dt)

replaced_dt = dt.replace(year=2025)
print(replaced_dt)

print(dt.tzinfo, dt.utcoffset())  # None, None つまり、 naive

aware_dt = dt.replace(tzinfo=ZoneInfo('America/Sao_Paulo'))
print(aware_dt.tzinfo, aware_dt.utcoffset())  # America/Sao_Paulo -1 day, 21:00:00 つまり、 aware

naive_dt = aware_dt.replace(tzinfo=None)
print(naive_dt.tzinfo, naive_dt.utcoffset())  # None, None つまり、 naive
