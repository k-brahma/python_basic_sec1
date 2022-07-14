"""
key が存在するかどうか確信が持たないときは get メソッドを使います

見つからなかったときは:
    第二引数を指定した場合は     : 第二引数の値を返す
    第二引数を指定しなかった場合は: None を返す

"""
fish_dict = {
    'karei': 15,
    'katsuo': 25,
    'fugu': 100,
}

print('same' in fish_dict)

# print(fish_dict['same']) #これはエラー

same_value = fish_dict.get('same', '見つかりませんでした')
print(same_value)

same_value = fish_dict.get('same')
print(same_value)

print('終了しました')
