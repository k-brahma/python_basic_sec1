"""
辞書の基本

辞書の作り方
    以下の2つのパターンがあります。
        my_dict = {}             #まずはこれを覚えましょう。
        my_dict = dict(**kwargs) #いずれ「すごく便利！」と思える日が来ます (^^*

辞書から key をキーに value を取り出すには、以下のように書きます
    my_value = my_dict[key]                    #key が絶対にある場合
    my_value = my_dict.get(key, default_value) #key　が存在しないかもしれない場合

辞書が特定の key を持つ要素を有しているかどうか調べるには、以下のように書きます
    key in my_dict

辞書にあとから key と value の組み合わせを追加するには？
    my_dict[key] = value #まずはこれを覚える
    my_dict.update(another_dict) #辞書の結合。慣れると便利！

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
