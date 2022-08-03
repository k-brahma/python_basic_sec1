## 日付時刻:

以下について学びます。

- 日付時刻のオブジェクト
- 日付のオブジェクト
- 時刻のオブジェクト(*)

日付時刻を大きく分類すると、以下の2つです。

- naive なもの
- awware なもの

naive, aware の違いは、タイムゾーン情報を含んでいるかどうかです。

日付時刻、日付を扱うには、 datetime モジュールを使います。  
datetime モジュールの主な登場人物は以下のとおりです。

| データ型               | 詳細                              |
|--------------------|---------------------------------|
| datetime.date      | 日付です。                    |
| datetime.datetime  | 日付と時刻を組み合わせたものです。               |
| datetime.timedelta | 2つの date または datetime の差分を表します。 |
| datetime.tzinfo    | タイムゾーン情報を扱う抽象クラスです。             |
| zoneinfo.ZoneInfo  | タイムゾーン情報を扱うクラスです。               |

***

datetime.datetime を例に、日付や時刻の作り方を以下に示します。

```python
from datetime import date, datetime

my_date = date(2022, 7, 22)
my_datetime = datetime(2022, 7, 22, 8, 27)

print(my_date)
print(my_datetime)
```

```python
import datetime

my_date = datetime.date(2022, 7, 22)
my_datetime = datetime.datetime(2022, 7, 22, 8, 27)

print(my_date)
print(my_datetime)
```

***

## tzdata の導入

タイムゾーン情報を扱うための方法はいくつかありますが、以下を使ってください。  
(よくあるトラブル含めて後述します)

```command
pip install tzdata
```

参考までに、利用可能なタイムゾーン情報の一覧を取得してみます。  
tzdata インストール前/インストール後で、結果を比較してみてください。

```python
import zoneinfo

zoneinfo.available_timezones()
```


