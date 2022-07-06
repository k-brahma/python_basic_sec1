"""
frozen setとは？
    set の、あとからの要素追加/削除不可能版

自分で作ることはまずありません。
「こういうものが存在する」ということのお知らせだけしておきます
"""
my_frozen_set = frozenset([1, 2, 3])
print(type(my_frozen_set))

print('終了しました')
