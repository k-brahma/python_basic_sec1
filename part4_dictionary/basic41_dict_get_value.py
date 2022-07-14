"""
辞書が特定の key を持つか調べるには in 演算子を使います
"""
fish_dict = {
    'karei': 15,
    'katsuo': 25,
    'fugu': 100,
}
print(fish_dict)
print(fish_dict['karei'])

# 辞書が特定の key を持つ要素を有しているかどうか調べます
print('karei' in fish_dict)
print('same' in fish_dict)

print(fish_dict['karei'])
print(fish_dict['same'])

print('終了しました')
