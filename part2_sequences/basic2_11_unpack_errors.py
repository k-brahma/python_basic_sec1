"""
やや高度な代入方法

アンパックに関連して、よくあるエラーを紹介
    1. 左辺と右辺で要素数があわない
    2. 左辺や右辺によけいなカンマ「 , 」がある

    上述のような問題に早く気づき、解決するには？
        [a] エラーメッセージを読む(慣れると、「あ、またやっちまったか」ですぐに解決できます)
        [b] 変数への値代入直後に type 関数で変数の中身の typeを調べてみる
        [c] 左辺の終わり/右辺の終わりに余計なカンマ「 , 」が無いかと、目を皿のようにして確認
            (もっとも、その前に[a]をやるように習慣づけたい)
"""

# 要素数が合わないとエラーになります
# a, b, c = 3, 5, 7, 9
# a, b, c, d = 3, 5, 7

# TypeError: can only concatenate tuple (not "int") to tuple
# 変数 y に 5 という値を入れたつもりが...
# y = 5,
# z = y + 7
# print(z)

# TypeError: cannot unpack non-iterable int object
# 変数 x に 5 という値をを入れたつもりが...
x, = 5

print('終了しました')
