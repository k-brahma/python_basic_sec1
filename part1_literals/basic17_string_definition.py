"""
タブと改行
タブや改行を含む文字列については、生成法をいくつか詳解
"""

pref = "神奈川県"
city = "横浜市"
ward = '中区元浜町'

# \t は [Tab] という意味
print(pref + '\t' + city + '\t' + ward)
print(f'{pref}\t{city}\t{ward}')

# \n は 改行 という意味
print(pref + '\n' + city + '\n' + ward)
print(f'{pref}\n{city}\n{ward}')

# 複数行の文字列を一気に生成するには？
full_address = """神奈川県
横浜市
中区元浜町"""
print(full_address)

# 複数行の f 文字列を生成
arg1 = "大理石"
arg2 = "夏"

full_string = f"""カルモジインの田舎は
{arg1}の産地で
そこで私は{arg2}を過ごしたことがあった
"""
print(full_string)

# 後述の「リスト」等を用いて、以下のような書き方をすることもできる
# (excel vba では Join 関数。 python では、文字列のメソッド)
my_list = [pref, city, ward]
result = '\n'.join(my_list)
print(result)
