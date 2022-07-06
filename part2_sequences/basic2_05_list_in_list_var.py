"""
リスト内の要素は何でも良いです。
もちろん、リスト内にリストを含むこともできます。

以下のサンプルコードでは、さきほどのサンプルコードを、変数を使って書き換えました。

q1 = ["jan", "feb", "mar", ]
q2 = ["apr", "may", "jun", ]
q3 = ["jul", "aug", "sep", ]
q4 = ["oct", "nov", "dec", ]
all_quoters = [q1, q2, q3, q4,]

all_quoters = [
    ["jan", "feb", "mar", ],
    ["apr", "may", "jun", ],
    ["jul", "aug", "sep", ],
    ["oct", "nov", "dec", ],
]

くりかえしますが、習得のためのアドバイスとして言えることは、慣れるまで、手を動かして書くことです。
そして、あまり疲れすぎない程度のことろで休憩し、しばらくしてから見直すことです。
"""
q1 = ["jan", "feb", "mar", ]
q2 = ["apr", "may", "jun", ]
q3 = ["jul", "aug", "sep", ]
q4 = ["oct", "nov", "dec", ]

all_quoters = [q1, q2, q3, q4, ]

print(all_quoters)

print(len(all_quoters))

for quater in all_quoters:
    print(quater)

for quater in all_quoters:
    for month in quater:
        print(month)

print('終了しました')
