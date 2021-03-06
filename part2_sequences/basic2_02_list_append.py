"""
リストの要素数を増やすときの代表的な方法は、以下の2つです。
    結合: lista + listb
    追加: list.append(要素)

「リストの要素を並べ替える」、「所定の条件にあうものだけを絞り込む」、
「リストから要素を削除する」、「要素を取り出してリストから削除する」等、
種々のハンドリング用のメソッドもあります。

ですが、ウェブプログラミングでは(ほぼ)使わないのでこのタイミングでは紹介しません。(*)

(*)
ウェブプログラミングでは、まとまった量のデータを取り扱うとすると、
そのデータは、データベースから取得する場合がほとんどです。

データベースからデータを取得する段階で、「必要最低限のものを、並べ替え済の状態で取得できている」
という状態にしていることが多く、そのため、
取得したデータを改めてフィルターしたり並べ替えたりする必要が生じることはあまりありません。
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
