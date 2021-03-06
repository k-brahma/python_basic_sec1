"""
比較演算子その1
    x < y      : x は y より小さい
    x <= y     : x は y より小さいか等しい
    x > y      : x は y より大きい
    x >= y     : x は y より大きいか等しい

    x == y     : x と y は等しい　              (*1)
    x != y     : x と y は等しくない            (*2)

    (*1) エクセルVBA以外触ったことがない方は、 = ではなく == だということに早く慣れましょう!!
    (*2) not x == y のほうが個人的には好み

    * x < y < z : x < y かつ y < z (python独特の書き方)
"""
# すべての演算子について紹介すると冗長すぎるので、
# 一部についてのみサンプルコードを紹介します

x = 3
y = 5
if x < y:
    print('条件を満たしました')
else:
    print('条件を満たしませんでした')

if x == y:
    print('同じです')
else:
    print('同じではありません')

if x != y:
    print('違います1')
else:
    print('違くないです1')

if not x == y:
    print('違います2')
else:
    print('違くないです2')

if 3 < y < 7:
    print('3 < y < 7 を満たしています')

print('終了しました')
