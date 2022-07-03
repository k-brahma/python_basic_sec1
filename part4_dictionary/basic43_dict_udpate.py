"""
辞書の基本

辞書にあとから key と value の組み合わせを追加するには？
    my_dict[key] = value #まずはこれを覚える
    my_dict.update(another_dict) #辞書の結合。慣れると便利！
"""

fish_dict = {
    'karei': 'カレイ',
    'katsuo': 'カツオ',
    'fugu': 'フグ',
}
print(fish_dict.get('maguro'))  # None

fish_dict['maguro'] = 'マグロ'
print(fish_dict.get('maguro'))  # マグロ

another_fish_dict = {
    'sake': '鮭',  # 新規
    'iwashi': '鰯',  # 新規
    'katsuo': '鰹',  # 更新
}

fish_dict.update(another_fish_dict)
print(fish_dict['karei'])
print(fish_dict['katsuo'])
print(fish_dict['iwashi'])
