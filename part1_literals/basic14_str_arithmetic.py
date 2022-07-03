"""
文字列の主な演算(事務職向けの超基本的なもの限定)

x + y  : 結合 (& ではない)
x * y  : 掛け算

注意点:
    文字列と数値は結合できない。
    文字列との結合にあたっては、数値は str 関数で明示的に文字列に変換する必要がある
"""

city = "横浜市"
ward = '中区元浜町'

print(city)
print(ward)

print(city + ward)
print(city + str(3))
print(city * 3)
