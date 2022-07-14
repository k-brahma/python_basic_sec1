"""
while 文

while 文は、 for 文に比してウェブプログラミングでは重要度が低いです。
    ここでは、さらっと紹介だけしておきます。

while 文の基本構成
    while [[条件]]:
        条件を満たしたときの処理
"""

# 今月の直前の月まで、各月を出力してみる
this_month = 7

i = 1
while i < this_month:
    print(i)
    print(f'{i}番目の月は{i}月です')
    i += 1

print('終了しました')
