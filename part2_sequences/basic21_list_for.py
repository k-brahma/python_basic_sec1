"""
リストとは？
    0個、1個、または複数の要素を含む集合体
    要素の順番情報持つ(後述の set 等は持たない)
    要素は重複してもOK(後述の set ではNG)
    一度定義したあとでも、要素の追加や削除ができる(後述の tuple ではできない)

    リストの作り方:
        my_list = [] #要素数 0 のリスト
        my_list = [要素] #要素数 1 のリスト
        my_list = [要素1, 要素2, 要素3, 要素4, 要素5, ... ] #複数要素を持つリスト
        my_list = [要素1, 要素2, 要素3,
                        要素4, 要素5, ... ] #途中改行しながら書いても良い

    要素は同じ型でなくて良い

    要素数を調べるには、 Len 関数

for 文の基本構成
    以下の書き方で、リスト等の「イテラブル(後述)」なオブジェクトを順番に処理できる
        for [変数] in [リストなどの、順番に値を取り出せるもの]:
            処理1
            処理2
            処理3
            ...

    pythonでは、for文の終わりは、「next」という言葉ではなく、「インデント」の終わりで表現します

"""

# 最後の要素のあとに注目。最後の要素のあと、カンマ「,」はあってもなくてもOK
pre_half_months = ["1月", "2月", "3月", "4月", "5月", "6月"]
post_half_months = ["7月", "8月", "9月", "10月", "11月", "12月", ]

# 要素数を調べるには len() 関数
print(len(pre_half_months))  # 6
print(len(post_half_months))  # 6

for month in pre_half_months:
    print(month)

for month in post_half_months:
    print(f'{month}は下半期の月のうちの1つです')

q1 = ["jan", "feb", "mar", ]
q2 = [
    "apr",
    "may",
    "jun",
]
q3 = [
    "jul",  # こんな感じにコメントを入れることもできる(便利！)
    "aug",  # 8月
    "sep",  # 9月
]
q4 = [  # こんな書き方もOK
    "oct", "nov",  # 10月と11月
    "dec"
]

all_quaters = [q1, q2, q3, q4]
for quater in all_quaters:
    for month in quater:
        print(month)
