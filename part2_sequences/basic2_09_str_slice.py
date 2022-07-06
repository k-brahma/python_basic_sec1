"""
pythonでは、文字列は、「文字のリスト」的なもの
    list, tuple と同様にスライスできる。
"""

my_str = "あいうえおかきくけこ"

# forループの対象にすると、1文字づつ取り出される(forループの対象にできる -> 「イテラブルである」と言います)
for char in my_str:
    print(char)

# 切り出しは slice で行います(先頭の要素のインデックスが 0 だということに注意！)
print(my_str[:3])  # 先頭0文字目から2文字目までを取りだす。
print(my_str[3:])  # 3文字目以降を取りだす。
print(my_str[3:7])  # 3文字目以降6文字目までを取りだす。

print(len(my_str))  # len関数で要素数を調べられるのは、 list, tuple と同様

print('終了しました')
