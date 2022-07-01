## 辞書:

辞書は、エクセルVBAの連想配列に近いものです。

key と value の対応があり、 dict[key] という構文で、 value を参照できます。

辞書の基本の形は、以下のようなものです。

```
my_dict = {
    key1: value1,
    key2: value2,
    key3: Value3,
}
```

キーは、それぞれユニークでなければなりません。

キーとして使えるのは、「イミュータブル」なオブジェクトのみです。  
と言っても、「イミュータブル」という言葉の意味についてはまだお伝えしていません。  
今の段階では、「文字列か数値を使っておけば間違いない」とだけ思っておいていただければOKです。