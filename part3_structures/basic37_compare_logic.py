"""
[[論理演算子]]
x or y     : x か y のどちらかを満たす
x and y    : x を満たし、 y を満たす(両方とも満たす必要あり)
not x      : x を満たさない (*5)

not はすでに登場しています。
or と and についてさらっと紹介します。

"""

post_half_months = ("7月", "8月", "9月", "10月", "11月", "12月")  # タプルです
ski_season_months = "11月", "12月", "1月", "2月"  # カッコをつけなくてもタプルです

if "12月" in post_half_months and "12月" in ski_season_months:
    print('12月は、下半期であって、スキーシーズンの月です')

hatsu_katuo_months = ('3月', '4月', '5月',)
modori_katuo_months = ('9月', '10月', '11月',)

if '10月' in hatsu_katuo_months or '10月' in modori_katuo_months:
    print('10月のカツオが水揚げされる月です')

print('終了しました')
