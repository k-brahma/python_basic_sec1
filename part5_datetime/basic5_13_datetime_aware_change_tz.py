"""
東京と、サンパウロについて、現在の日付時刻を取得します。
出力は、指定された　timezone の日付として行われます。

後半では、サンパウロ時間の日付時刻を、シンガポール時間に変換しています。
内部的な値に変更はありません。表示が変わるだけです。
"""
from datetime import datetime
from zoneinfo import ZoneInfo

tokyo_now = datetime.now(ZoneInfo('Asia/Tokyo'))
print(tokyo_now)
print(tokyo_now.tzinfo)
print(tokyo_now.utcoffset())

sao_paolo_now = datetime.now(ZoneInfo('America/Sao_Paulo'))
print(sao_paolo_now)
print(sao_paolo_now.tzinfo)
print(sao_paolo_now.utcoffset())

singapore_now = sao_paolo_now.astimezone(tz=ZoneInfo('Asia/Singapore'))
print(singapore_now)
print(singapore_now.tzinfo)
print(singapore_now.utcoffset())

print(sao_paolo_now == singapore_now)  # sao_paolo_now と singapore_now は同じ値
