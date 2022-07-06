"""
セットとは？
    0個、1個、または複数の要素を含む集合体
    要素の順番情報を持たない(list, tuple 等は持つ) -> 取り出すときに順序が保証されない
    要素は重複しない(list, tuple では重複OK)
    listのappendに相当するようなメソッドがあり、一度定義したあとでも、要素の追加や削除ができる

    セットの作り方:
        my_set = {要素1, 要素2, 要素3, 要素4, 要素5, ... }
        my_set = set([要素1, 要素2, 要素3, 要素4, 要素5, ... ]) #リスト/タプル等から

なお、自分で作ることはほぼありません。
あえて言うなら、重複したリストを整理するのに便利です。ただし、順序は破壊されます。
"""

# {} でセットを作る
pre_half_months = {"1月", "2月", "3月", "4月", "5月", "6月", }

print(pre_half_months)
print(type(pre_half_months))
for month in pre_half_months:
    print(month)

# リストを引数にして作る
half_months_list = ["7月", "8月", "9月", "10月", "11月", "12月"]
post_half_months = set(half_months_list)

print(type(post_half_months))
for month in post_half_months:
    print(f'{month}は下半期の月のうちの1つです')

# 追加してみる listでは append だったが、 set では add
months = {"jan", "feb", "mar", "apr", "may", }
months.add('jun')

# 要素数を調べるにはやはり len関数
print(len(months))

# 重複したリストを整理してみる
redundant_list = ["jan", "feb", "mar", "jan", "jan", "feb", ]
new_set = set(redundant_list)
print(new_set)

print('終了しました')
