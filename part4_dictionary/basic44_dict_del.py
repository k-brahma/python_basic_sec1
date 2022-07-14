"""
辞書内の key と value の組み合わせを削除する方法については、
まず、は以下の del 文を覚えてください。
    del my_dict[key]

"""

fish_dict = {
    'karei': 15,
    'katsuo': 25,
    'fugu': 100,
}
print(fish_dict)

del fish_dict["karei"]
print(fish_dict)

print('終了しました')
