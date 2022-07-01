"""
format関数
    f文字列以前からあるもの。
        紹介した目的:
            状況によりf文字列よりもすっきり書けることがあるので、必要に応じて使う
            古いコード内で見かけても驚かないようにする
"""

city = "横浜市"
ward = '中区元浜町'
f_str = f'神奈川県 {0} {1}３丁目２１−２'.format(city, ward)
print(f_str)

this_year = 2020
this_year_full_string = '今年は {0} 年'.format(this_year)
print(this_year_full_string)

next_month_full_string = '来年は{}年です'.format(this_year + 1)
print(next_month_full_string)
