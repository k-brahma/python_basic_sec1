"""
文字列の生成(その2)

formatメソッド
    f文字列以前からあるもの。
        紹介した目的:
            状況によりf文字列よりもすっきり書けることがあるので、必要に応じて使う
            古いコード内で見かけても驚かないようにする
"""

city_name = "横浜市"
full_address = '神奈川県{0}中区元浜町３丁目２１−２'.format(city_name)
print(full_address)

# 複数差し込むことも可能です。複数の場合は{}の中にインデックス番号を記入します
pref_name = "神奈川県"
weather = "晴れ"
forecast = '今日の{0}の天気は{1}でしょう'.format(city_name, weather)
print(forecast)

# f文字列では、{}内の値の型は気にしなくてよい(強制的に文字列として扱われる)
this_year = 2022
this_year_full_string = '今年は{0}年'.format(this_year)
print(this_year_full_string)

# {}内で演算もできる(ただし、あまりやりたくない)
next_month_full_string = '来年は{0}年です'.format(this_year + 1)
print(next_month_full_string)

print('終了しました')
