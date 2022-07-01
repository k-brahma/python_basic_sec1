"""
変数とは？
    初心者向けに極めて乱暴な説明をすると、以下のような「言い換え」をできるようになります
        a = 17 : 「a といえば 17 のこと」という意味。
        b = 5  : 「b といえば  5 のこと」という意味。

        * a = 17 であれば、「17」という値に「a」という名札をつけるようなイメージ
            IT用語で「参照」と言います

        Pythonで変数を使って「参照」できるもの:
            数値や文字のようなデータ型
            クラスのインスタンス
            関数
            クラス
            モジュール
            ...

    変数の参照先は、何度でも変更できます
        c = 9 : 「c といえば 9 のこと」という意味。
        c = 2 : 「a といえば 2 のこと」という意味。
        ↓
        以後、c といえば 2 のこと。(9ではない)

    変数名を決めるときの注意:
        Python では、変数は、小文字で書くのが作法
        複数の英単語をつなぐときは _ (アンダースコア)でつなぐのが作法
        日本語は避けるのが作法(「どうしても日本語にしたい」ということであれば、止めませんが)
"""

a = 17
b = 5
c = a - b  # 17 - 5 の計算結果は12ですね。

print(a)  # 17と出力されます。「a といえば17のこと」だからです。
print(b)  # 5と出力されます。「b といえば 5のこと」だからです。
print(c)  # 12と出力されます。「c といえば 12のこと」だからです。

print(a + b + 5)  # こんな計算もOK

# 変数が指し示す値を、変更します
a = 7
b = 3

print(a)  # 7と出力されます。今となっては、「a といえば7のこと」だからです。
print(b)  # 3と出力されます。今となっては、「b といえば3のこと」だからです。
print(c)  # 注意！4ではなく、12と出力されます。cについては、「c といえば 12のこと」のままだからです。

print(a + b + c)  # 22 と出力されます。

# 変数名は半角小文字で作りましょう。
this_year = 2022

print(this_year)
