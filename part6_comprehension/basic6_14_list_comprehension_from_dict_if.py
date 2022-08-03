"""
内包表記内に、if 文を含めることもできます

以下では、12星座を、 animail, human, hybrid の3つのタイプに分けてみました。
そして、 type = "animal" のものだけ出力してみました。

* あまり複雑な条件文は含められません
"""
base_dic = {
    "やぎ座": {"type": "animal", "month": 1, "day": 19},
    "みずがめ座": {"type": "human", "month": 2, "day": 18},
    "うお座": {"type": "animal", "month": 3, "day": 20},
    "おひつじ座": {"type": "animal", "month": 4, "day": 19},
    "おうし座": {"type": "animal", "month": 5, "day": 20},
    "ふたご座": {"type": "human", "month": 6, "day": 21},
    "かに座": {"type": "animal", "month": 7, "day": 22},
    "しし座": {"type": "animal", "month": 8, "day": 22},
    "おとめ座": {"type": "human", "month": 9, "day": 22},
    "てんびん座": {"type": "human", "month": 10, "day": 23},
    "さそり座": {"type": "animal", "month": 11, "day": 21},
    "いて座": {"type": "hybrid", "month": 12, "day": 21},
}

name_list1 = []
for key, value in base_dic.items():
    if value['type'] == "animal":
        name_list1.append(key)
print(name_list1)

name_list2 = [key for key, value in base_dic.items() if value['type'] == "animal"]
print(name_list2)
