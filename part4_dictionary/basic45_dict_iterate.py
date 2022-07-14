"""
辞書 と for 文
"""

fish_dict = {
    'karei': 15,
    'katsuo': 25,
    'fugu': 100,
}

for key in fish_dict.keys():
    print(key)

for value in fish_dict.values():
    print(value)

for key, value in fish_dict.items():
    print(f'{key}が{value}匹います')

print('終了しました')
