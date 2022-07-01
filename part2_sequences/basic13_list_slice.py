"""
スライス

リストの要素の取得: (先頭は「0番目」として数える)
    list[index] #index番目
    list[-index] #後ろから、index番目の一個手前まで(クセあり、注意！)
    list[:index] #先頭から、index番目まで

"""

# 最後の要素のあとに注目。最後の要素のあと、カンマ「,」はあってもなくてもOK
all_months = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月", ]

third_month = all_months[2]
print(third_month)

latter_secnod_month = all_months[-2]  # -1 は 12月、 - 2 は 11月
print(latter_secnod_month)

first_three_months = all_months[:3]  # 0, 1, 2番目まで(3番目は含まない)
print(first_three_months)

first_three_months_with_zero = all_months[0:3]  # 直前に紹介した [:3] と同じ。コロンの前の 0 が省略された
print(first_three_months_with_zero)

after_three_months = all_months[3:]  # index番号3以降すべて
print(after_three_months)

step_3 = all_months[1:10:3]  # index番号1番から9番までを、3個置きに(1, 4, 7 番目)。(使いこなせなくてOKです)
print(step_3)
