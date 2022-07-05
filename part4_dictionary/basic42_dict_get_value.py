"""
辞書の基本

辞書の作り方
    以下の2つのパターンがあります。
        my_dict = {}     #まずはこれを覚えましょう。
        my_dict = dict() #いずれ「すごく便利！」と思える日が来ます (^^*

辞書から key をキーに value を取り出すには、以下のように書きます
    my_value = my_dict[key]                    #key が絶対にある場合
    my_value = my_dict.get(key, default_value) #key　が存在しないかもしれない場合

辞書が特定の key を持つ要素を有しているかどうか調べるには、以下のように書きます
    key in my_dict

"""

my_dict1 = {
    'a': 3,
    'b': 5,
    'c': 7,
}
print(my_dict1['b'])

my_dict2 = dict(m='morning', a='after noon', n='night')
print(my_dict2['a'])

fish_dict = {
    'karei': 'カレイ',
    'katsuo': 'カツオ',
    'fugu': 'フグ',
}

# 存在しないキーを指定するとエラーになる
# my_fish0 = fish_dict['hirame']

# .getでキーが見つかった場合
my_fish1 = fish_dict.get('karei', '魚')  # 第1引数はキー、第2引数はキーが見つからなかったとき用の初期値
print(my_fish1)

# .getでキーが見つからなかった場合
my_fish2 = fish_dict.get('iwashi', '魚')
print(my_fish2)

# .getで第2引数を省略した場合はNoneが返る
my_fish3 = fish_dict.get('maguro', )
print(my_fish3)

# 辞書が特定の key を持つ要素を有しているかどうか調べます
print('karei' in fish_dict)
print('same' in fish_dict)

print('終了しました')
