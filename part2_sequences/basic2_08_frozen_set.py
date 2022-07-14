"""
frozen setとは？
    set の、あとからの要素追加/削除不可能版

自分で作ることはまずありません。
「こういうものが存在する」ということのお知らせだけしておきます
"""
my_frozen_set = frozenset(["a", "b", "c", "d", "e"])
print(type(my_frozen_set))
for elem in my_frozen_set:
    print(elem)

print('終了しました')
