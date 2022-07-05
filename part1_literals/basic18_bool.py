"""
True/False のいずれかの値を取る bool型 は、比較演算で使います。

ここでは、 bool 関数を紹介します。
bool 関数は、引数を渡すと、 True/False のいずれかの値を返します。
"""

a = True
print(a)

b = False
print(b)

result = bool(1)
print(result)  # True

result = bool(0)
print(result)  # False

result = bool(-1)
print(result)  # True

result = bool("文字列")
print(result)  # True

result = bool("")  # 長さ0の文字列
print(result)  # False

result = bool(None)
print(result)  # False

print('終了しました')
