"""
リストの要素を追加するときの代表的な方法は、以下の2つ
    lista + listb ()
    list.append(要素)

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
