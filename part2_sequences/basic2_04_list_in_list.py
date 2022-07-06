"""
リスト内の要素は何でも良いです。
もちろん、リスト内にリストを含むこともできます。以下の要領です。

all_quoters = [
    ["jan", "feb", "mar", ],
    ["apr", "may", "jun", ],
    ["jul", "aug", "sep", ],
    ["oct", "nov", "dec", ],
]

エクセルVBAでは、セルに値を放り込んでおけば複雑な構造を変数に格納する必要はありませんでした。
Pythonではそうもいきません。変数の中身がややこしい構造になることもままあります。
ここは肚のくくりどころです (^^;

習得のためのアドバイスとして言えることは、慣れるまで、手を動かして書くこと。
そして、あまり疲れすぎない程度のことろで休憩し、しばらくしてから見直すことです。
"""
all_quoters = [
    ["jan", "feb", "mar", ],
    ["apr", "may", "jun", ],
    ["jul", "aug", "sep", ],
    ["oct", "nov", "dec", ],
]
print(len(all_quoters))  # 要素数は4

for quater in all_quoters:
    print(quater)  # どれも要素数は3

for quater in all_quoters:
    for month in quater:
        print(month)

print('終了しました')
