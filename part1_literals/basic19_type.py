"""
Pythonプログラミングでは、データの「型」に敏感でありたい
    実際、デバッグ時に型を調べることは頻繁にある

以下で、データの「型」にかかる調査をしてみる
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

# None型であることの確認には、 Is 演算子(後述)を使うのが一般的
print(my_none_value is None)  # True
