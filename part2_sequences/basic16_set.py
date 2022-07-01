"""
セットとは？
    0個、1個、または複数の要素を含む集合体
    要素の順番情報持たない(list, tuple 等は持つ) -> 取り出すときに順序が保証されない
    要素は重複しない(list, tupl では重複OK)
    listのappendに相当するようなメソッドがあり、一度定義したあとでも、要素の追加や削除ができる

    セットの作り方:
        my_set = set(要素1, 要素2, 要素3, 要素4, 要素5, ... )
        my_set ={ [要素1, 要素2, 要素3, 要素4, 要素5, ...] } #リストから
        my_set ={ (要素1, 要素2, 要素3, 要素4, 要素5, ...) } #タプルから

なお、自分で作ることはほぼありません。
あえて言うなら、重複したリストを整理するのに便利。(だが、順序は破壊される)
"""

# 最後の要素のあとに注目。最後の要素のあと、カンマ「,」はあってもなくてもOK
pre_half_months = set(["1月", "2月", "3月", "4月", "5月", "6月"])
post_half_months = {"7月", "8月", "9月", "10月", "11月", "12月", }

# 以下の2つは同じ出力結果(型が同じだから)
print(type(pre_half_months))
print(type(post_half_months))

for month in pre_half_months:
    print(month)

for month in post_half_months:
    print(f'{month}は下半期の月のうちの1つです')

months = {"jan", "feb", "mar", "apr", "may", }
months.add('jun')

print(len(months))

# 重複したリストを整理してみる
redundant_list = ["jan", "feb", "mar", "jan", "jan", "feb", ]
new_set = set(redundant_list)
print(len(redundant_list), len(new_set))
