"""
pythonでは、文字列は、「文字のリスト」的なもの
    list, tuple, set と同様にスライスできる。
"""

my_str = "あいうえおかきくけこ"

# forループの対象にすると、1文字づつ取り出される(forループの対象にできる -> 「イテラブルである」と言います)
for char in my_str:
    print(char)

# 切り出しは slice で行います(先頭の要素のインデックスが 0 だということに注意！)
print(my_str[:3])  # 先頭0文字目から2文字目までを取りだす。
print(my_str[3:])  # 3文字目以降を取りだす。
print(my_str[3:7])  # 3文字目以降6文字目までを取りだす。

# ついでに、文字列にかかる基礎的な関数、メソッドを紹介
print(len(my_str))  # len関数で要素数を調べられるのは、 list, tuple と同様

replaced = my_str.replace('abc', '神奈川県横浜市')  # replace は、関数ではなく、文字列のメソッドとして実装されている
print(replaced)  # 神奈川県横浜市defghijk

find_result = my_str.find('efg')  # 文字列内を検索する find も、関数ではなく、文字列のメソッドとして実装されている
print(find_result)  # 4

print('終了しました')
