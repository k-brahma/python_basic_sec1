"""
format文字列
    以下のような書き方で、文字列内に変数の値を簡単に挿入できる
        f'文字列' または f"文字列"
"""

city = "横浜市"
ward = '中区元浜町'
f_str = f'神奈川県{city}{ward}３丁目２１−２'
print(f_str)

# f文字列では、{}内の値の型は気にしなくてよい(強制的に文字列として扱われる)
this_year = 2020
this_year_full_string = f'今年は{this_year}年'
print(this_year_full_string)

# {}内で演算もできる(ただし、あまりやりたくない)
next_month_full_string = f'来年は{this_year + 1}年です'
print(next_month_full_string)
