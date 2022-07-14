"""
辞書にあとから key と value の組み合わせを追加するには？(上書きもこれでOK)
    my_dict[key] = value         # 要素の追加。まずはこれを覚える
    my_dict.update(another_dict) # 辞書の結合。慣れると便利！
"""

fish_dict = {
    'karei': 15,
    'katsuo': 25,
    'fugu': 100,
}
print(fish_dict.get('maguro'))  # None

fish_dict['maguro'] = 3  # 新規
print(fish_dict)

fish_dict['fugu'] = 77  # 更新
print(fish_dict)

another_fish_dict = {
    'sake': 91,  # 新規
    'iwashi': 92,  # 新規
    'katsuo': 93,  # 更新
}

fish_dict.update(another_fish_dict)
print(fish_dict['karei'])
print(fish_dict['katsuo'])
print(fish_dict['iwashi'])

print('終了しました')
