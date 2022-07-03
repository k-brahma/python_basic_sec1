"""
辞書 と for 文
    辞書の key のリストを順番に処理する
        for kei in  mydict.keys()
            ...

    辞書の value のリストを取得する
        for value in mydict.values()
            ...

    辞書の key, value の tuple のリストを取得する
        for item in mydict.item()
            ... # item は、 (key, value) という tuple

    というか、以下のほうが普通(tuple の unpack)
        for key, value in mydict.items():
            ...

    .keys(), .values(), .items() のいずれも、出力順序は保証されています。
    具体的に言うと、定義した順序に従います(*1)

(*1)
古いバージョンの python では保証されていませんでした。
その点、ネットで過去記事を読むときは、気をつけてください。
また、開発歴が長いライブラリでは、「出力順序は保証された辞書」として「OrderedDict」なのもの等が
使われている場合があります。
"""

fish_dict = {
    'karei': 'カレイ',
    'katsuo': 'カツオ',
    'fugu': 'フグ',
}
for key in fish_dict.keys():
    print(key)

for value in fish_dict.values():
    print(value)

for item in fish_dict.items():
    print(item)

for key, value in fish_dict.items():
    print(f'key: {key}')
    print(f'value: {value}')
