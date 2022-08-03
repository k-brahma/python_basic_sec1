# 内包表記:

内包表記 (comprehension) を使うと、リスト、セット、辞書を簡潔な記述で生成できる。  
より簡潔に記述でき、処理速度はわずかに高速です。

このセクションでのリライト例を理解できるには、list や辞書を内包表記でない通常の書き方で書けることが前提です。  
難しいと感じられたようでしたら、セクション2の復習をしっかり行い、それからここに戻ってきてください。

***

## リスト内包表記

```python
# リスト内包表記の典型例:
result_list = [item for item in items]
```

```python
# 上記は以下と同じです。
result_list = []
for item in items:
    result_list.append(item)
```

```python
# 条件文を含めることもできます
result_list = [item for item in items if condition]
```

```python
# 上記は以下と同じです。
result_list = []
for item in items:
    if condition:
        result_list.append(item)
```

***

## 辞書内包表記

```python
# 辞書内包表記の典型例:
result_dict = {key: value for item in items}
```

```python
# 上記は以下と同じです。
result_dict = {}
for item in items:
    result_dic[key] = value
```

```python
# 条件文を含めることもできます
result_dict = {key: value for item in items if condition}
```

```python
# 上記は以下と同じです。
result_dict = {}
for item in items:
    if condition:
        result_dic[key] = value
```
