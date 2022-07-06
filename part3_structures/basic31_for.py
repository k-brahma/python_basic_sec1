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
        イテラブルオブジェクト一般
"""

pre_half_months = ["1月", "2月", "3月", "4月", "5月", "6月"]

for month in pre_half_months:
    print(month)

# 実は文字列もfor文で処理可能
target_string = 'リストなどの、順番に値を取り出せるもの'
for char in target_string:
    print(char)

print('終了しました')
