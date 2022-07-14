# 辞書

## 基本操作

1. 作り方

```python
my_dict = {}  # まずはこれを覚えましょう。
my_dict = dict()  # いずれ「すごく便利！」と思える日が来ます (^^*
```

2. key をキーに値を取得します

```python
my_value = my_dict[key]  # key が絶対にある場合
my_value = my_dict.get(key, default_value)  # key　が存在しないかもしれない場合
```

3. 辞書が特定の key を持つか調べます

```python
result = key in my_dict
```

4. 辞書にあとから key と value の組み合わせを追加します(上書きも同様です)

```python
my_dict[key] = value  # まずはこれを覚える
my_dict.update(another_dict)  # 辞書の結合。慣れると便利！
```

5. 辞書内の key と value の組み合わせを削除するには

```python
del my_dict[key]  # まずはこれを覚える
```

***

## 辞書と for 文

辞書の key のリストを順番に処理します

```python
for key in mydict.keys():
    処理
    処理
    処理
```

辞書の value のリストを取得します

```python
for value in mydict.values():
    処理
    処理
    処理
```

辞書の key, value の tuple のリストを取得します

```python
for key, value in mydict.items():
    処理
    処理
    処理
```

.keys(), .values(), .items() のいずれも、出力順序は保証されています。  
具体的に言うと、定義した順序に従います(*1)

(*1)
古いバージョンの python では保証されていませんでした。  
その点、ネットで過去記事を読むときは、気をつけてください。  
また、開発歴が長いライブラリでは、「出力順序は保証された辞書」として「OrderedDict」なのもの等が使われている場合があります。
