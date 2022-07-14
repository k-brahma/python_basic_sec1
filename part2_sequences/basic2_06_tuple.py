"""
タプルとは？
    0個、1個、または複数の要素を含む集合体
    要素の順番情報を持つ(後述の set 等は持たない)
    要素は重複してもOK(後述の set ではNG)
    listのappendに相当するようなメソッドがなく、一度定義すると、要素の追加や削除ができない
        * タプルとタプルを + で結合して新しいタプルを作ることはできる

    タプルの作り方:
        my_tuple = () # 要素0のものをあえて作るならばこういう書き方(使い道はないが)
        my_tuple = 要素1, #カンマがある
        my_tuple = 要素1, 要素2, 要素3, 要素4, 要素5, ...
        my_tuple = (要素1, 要素2, 要素3, 要素4, 要素5, ... ) #カッコでくくってもOK

    リストとタプルの使い分け
        リスト:
            「とりあえず定義したけど、コード内で要素の追加/削除がありそう」というとき
        タプル:
            「たとえうっかりでも、コード内で要素の追加/削除があったら困る」というとき
            さらに言うと、タプルのほうが若干高速に処理可能ではあります

    「変数に数値や文字列を格納しようとしたのに、文の末尾に , カンマがあってタプルになってしまう」
    というのはpythonあるあるです。
    特に、コピー＆ペーストで文や変数をもってきたときにやってしまいがちです。
"""

# 型を見てみよう
blank_list = []
print(type(blank_list))  # <class 'list'>

blank_tuple = ()
print(type(blank_tuple))  # <class 'tuple'>

one_elem_tuple = 3,  # tuple です。末尾のカンマに注目！
print(type(one_elem_tuple))

# 要素の追加/削除ができないこと以外はリストとほぼ同じと思っておいていただいてOKです

# リスト
month_list = ["jan", "feb", "mar"]
print(type(month_list))
month_list.append("apr", )  # これはOK。 listだから。
print(len(month_list))  # 4

# タプル
month_tuple = "jul", "aug", "sep",
print(type(month_tuple))
# month_tuple.append("oct", )  # これはNG。 tupleへの要素追加はできない

print('終了しました')
