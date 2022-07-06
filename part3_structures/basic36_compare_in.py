"""
比較演算子その2
    x in y     : x は y に含まれている
    x not in y : x は y に含まれていない

    x is y     : x と y は同じオブジェクト　     (*3)
    x is not y : x と y は同じオブジェクトでない　(*3)

y に来るのは、「イテラブル」なオブジェクト。
すなわち、ここまでに学んできた中で言えば...
    リスト
    タプル
    set
    frozenset
    文字列
"""
# すべての演算子について紹介すると冗長すぎるので、
# 「受講生はエクセルVBAである程度慣れている」という前提で、
# 極力簡潔なサンプルコードを載せます

pre_half_months_list = ["1月", "2月", "3月", "4月", "5月", "6月"]
print(type(pre_half_months_list))
if "3月" in pre_half_months_list:
    print('3月　は list の中にありました')

post_half_months_tuple = ("7月", "8月", "9月", "10月", "11月", "12月",)
print(type(post_half_months_tuple))
if "3月" not in post_half_months_tuple:
    print('3月　は tuple の中にありませんでした')

pre_half_months_set = {'jan', 'feb', 'mar', 'apr', 'may', 'jun'}
print(type(pre_half_months_set))
if 'mar' in pre_half_months_set:
    print('mar は set の中にありました')

my_str = 'カルモジインの田舎は大理石の産地でそこで私は夏を過ごしたことがあった'
print(type(my_str))
if '秋' not in my_str:
    print('秋 は 文字列 の中にありませんでした')
if '夏' in my_str:
    print('夏 は 文字列 の中にありました')
if '大理石' in my_str:
    print('大理石 は 文字列 の中にありました')

print('終了しました')
