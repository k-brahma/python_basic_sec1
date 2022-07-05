"""
文字列の生成(その3)

タブと改行
    タブや改行を含む文字列については、生成法をいくつか紹介します

複数行の文字列を生成する方法を紹介します
"""

# \t は [Tab] という意味
tab_string = "神奈川県\t横浜市\t中区元浜町"
print(tab_string)

# \n は 改行 という意味
multiline_string = "神奈川県\n横浜市\n中区元浜町"
print(multiline_string)

# 複数行の文字列を一気に生成するには？
full_address = """神奈川県
横浜市
中区元浜町"""
print(full_address)

# f文字列で複数行の文書に差し込みをする
arg1 = "大理石"
arg2 = "夏"

full_string = f"""カルモジインの田舎は
{arg1}の産地で
そこで私は{arg2}を過ごしたことがあった
"""
print(full_string)

# 後述の「リスト」等を用いて、以下のような書き方をすることもできる
pref = "神奈川県"
city = "横浜市"
ward = "中区"

my_list = [pref, city, ward]
result = '\n'.join(my_list)
print(result)

print('終了しました')
