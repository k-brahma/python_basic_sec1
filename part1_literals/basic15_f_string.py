"""
文字列の生成(その1)

f文字列
    以下のような書き方で、文字列内に変数の値を簡単に挿入できる
        f'文字列' または f"文字列"
"""

city_name = "横浜市"
full_address = f'神奈川県{city_name}中区元浜町３丁目２１−２'
print(full_address)

# 複数差し込むことも可能です
pref_name = "神奈川県"
weather = "晴れ"
forecast = f'今日の{pref_name}の天気は{weather}でしょう'
print(forecast)

# f文字列では、{}内の値の型は気にしなくてよい(強制的に文字列として扱われる)
this_year = 2022
this_year_full_string = f'今年は{this_year}年'
print(this_year_full_string)

# {}内で演算もできる(ただし、あまりやりたくない)
next_month_full_string = f'来年は{this_year + 1}年です'
print(next_month_full_string)

print('終了しました')
