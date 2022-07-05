"""
リスト内の要素は何でも良いです。
もちろん、リスト内にリストを含むこともできます。

以下のサンプルコードでは、 *1 のタイミングで、変数 all_quoters の中身はこうなっています。

all_quoters = [
    ["jan", "feb", "mar", ],
    ["apr", "may", "jun", ],
    ["jul", "aug", "sep", ],
    ["oct", "nov", "dec", ],
]

エクセルVBAではセルに値を放り込んでおけば複雑な構造を変数に格納する必要はありませんでした。
Pythonではそうもいきません。ここは肚くくりどころです (^^;

習得のためのアドバイスとして言えることは、慣れるまで、手を動かして書くこと。
そして、あまり疲れすぎない程度のことろで休憩し、しばらくしてから見直すことです。
"""
q1 = ["jan", "feb", "mar", ]
q2 = ["apr", "may", "jun", ]
q3 = ["jul", "aug", "sep", ]
q4 = ["oct", "nov", "dec", ]

all_quoters = [q1, q2, q3, q4, ]  # *1
print(len(all_quoters))  # 要素数は4

for quater in all_quoters:
    print(len(quater))  # どれも要素数は3

for quater in all_quoters:
    for month in quater:
        print(month)

print('終了しました')
