"""
aware な時間、 naive な時間ともに、 datetime.datetime クラスのオブジェクトです。

"""
from datetime import datetime
from zoneinfo import ZoneInfo

naive_dt = datetime(2022, 8, 1, 13, 15, 0)
aware_dt = datetime(2022, 8, 1, 13, 15, 0, tzinfo=ZoneInfo('America/Sao_Paulo'))

print(type(naive_dt), type(aware_dt))
print(type(naive_dt) == type(aware_dt))
