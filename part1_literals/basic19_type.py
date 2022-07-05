"""
Pythonプログラミングでは、データの「型」に敏感でありたい
    実際、デバッグ時に型を調べることは頻繁にある

以下で、データの「型」にかかる調査をしてみる

type関数       : 引数として指定されたオブジェクトの型を取得する
isinstance関数 : 第一引数にオブジェクト、第二引数に型を指定する。戻り値は bool型(True/False)
"""

# 文字列

full_address = "神奈川県横浜市中区元浜町3-21-2"

print(type(full_address))  # <class 'str'> と出力される

print(isinstance(full_address, str))  # Trueと出力される

# 数値
my_number = 100

print(type(my_number))  # <class 'int'>

print(isinstance(my_number, int))  # True

print(isinstance(my_number, str))  # False

# None
my_none_value = None

print(type(my_none_value))  # <class 'NoneType'>

# None型であることの確認には、 is 演算子(後述)を使うのが一般的
print(my_none_value is None)  # True

print('終了しました')
