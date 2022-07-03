"""
for 文でよくある形(その1)

for 文の基本構成
    for [変数] in [リストなどの、順番に値を取り出せるもの]:
        処理1
        処理2
        処理3
        ...

「リストなどの、順番値を取り出せるもの」について:
    すでに紹介したもの:
        list, tuple, set
    実はこれに該当するもの
        文字列
    ほか、初心者的に押さえておきたいもの
        辞書(後述)
    さきざき理解しておきたいもの
        ジェネレータ
        イテラブルオブジェクト


数値を使いたいときのパターン2つ:

その1: 単純に数字だけで処理したい
    for i in range(0, 11):  # 0から10までくり返す
        処理1
        処理2
        処理3
        ...

その2: 「リストなどの、順番値を取り出せるもの」を扱うときにインデックスを渡したい
    for i, elem in enumerate(iterable):
        処理1
        処理2
        処理3
        ...
"""

pre_half_months = ["1月", "2月", "3月", "4月", "5月", "6月"]

for month in pre_half_months:
    print(month)

# 実は文字列もfor文で処理可能
target_string = 'リストなどの、順番に値を取り出せるもの'
for char in target_string:
    print(char)

for i in range(0, 11):  # 0から10までくり返す
    print(i)

post_half_months = ["7月", "8月", "9月", "10月", "11月", "12月", ]
for i, month in enumerate(post_half_months):
    print(f'下半期の{i + 1}番目の月は{month}です')

for i, month in enumerate(post_half_months, start=1):  # startを指定するともっとスマートに書ける
    print(f'下半期の{i}番目の月は{month}です')
