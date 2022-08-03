"""
UTC を指定する方法は？
    timezone.utc を指定します

astimezone で tz=None を指定すると？
    ローカル環境の timezone が選択されます
"""
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

utc_now = datetime.now(timezone.utc)
print(utc_now)
print(utc_now.tzinfo)
print(utc_now.utcoffset())

sao_paolo_now = datetime.now(ZoneInfo('America/Sao_Paulo'))

local_now = sao_paolo_now.astimezone(tz=None)
print(local_now)
print(local_now.tzinfo)
print(local_now.utcoffset())
