"""
やや高度な代入方法

複数の変数に同一の値を投入するとき、以下のように書ける
    x = y = z = None

アンパック
    受け取り側の変数を tuple として並べて記述できる
        a, b, c = 3, 5, 7
"""

x = y = z = None
print(x)
print(y)
print(z)

a, b, c = 3, 5, 7
print(a)
print(b)
print(c)

x, y, z = [1, 2, 3]
print(x)
print(y)
print(z)

# 番外編 文字列は「文字のリスト」のようなものなので、こんな unpack も可能です
# 実務では使いません
p, q, r = "あいう"
print(p)
print(q)
print(r)

print('終了しました')
