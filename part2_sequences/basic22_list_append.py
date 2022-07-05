"""
リストの要素を追加するときの代表的な方法は、以下の2つ
    結合: lista + listb ()
    追記: list.append(要素)

「リストから要素を削除する」、「要素を取り出してリストから削除」等、種々のハンドリング用のメソッドもあるが
ウェブプログラミングでは(ほぼ)使わないのでこのタイミングでは紹介しません。
"""

# 最後の要素のあとに注目。最後の要素のあと、カンマ「,」はあってもなくてもOK
pre_half_months = ["1月", "2月", "3月", "4月", "5月", "6月"]
post_half_months = ["7月", "8月", "9月", "10月", "11月", "12月", ]

all_months = pre_half_months + post_half_months

for month in all_months:
    print(month)

month_list = ["jan", "feb", "mar", ]
month_list.append('apr')

print(len(month_list))
for month in month_list:
    print(month)

print('終了しました')
