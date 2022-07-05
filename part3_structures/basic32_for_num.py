"""
for 文でよくある形(その2)

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

for i in range(0, 11):  # 0から10までくり返す
    print(i)

post_half_months = ["7月", "8月", "9月", "10月", "11月", "12月", ]
for i, month in enumerate(post_half_months):
    print(f'下半期の{i + 1}番目の月は{month}です')

for i, month in enumerate(post_half_months, start=1):  # startを指定するともっとスマートに書ける
    print(f'下半期の{i}番目の月は{month}です')

print('終了しました')
