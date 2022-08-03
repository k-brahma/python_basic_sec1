base_dic = {
    1: {"name": "やぎ座", "month": 1, "day": 19},
    2: {"name": "みずがめ座", "month": 2, "day": 18},
    3: {"name": "うお座", "month": 3, "day": 20},
    4: {"name": "おひつじ座", "month": 4, "day": 19},
    5: {"name": "おうし座", "month": 5, "day": 20},
    6: {"name": "ふたご座", "month": 6, "day": 21},
    7: {"name": "かに座", "month": 7, "day": 22},
    8: {"name": "しし座", "month": 8, "day": 22},
    9: {"name": "おとめ座", "month": 9, "day": 22},
    10: {"name": "てんびん座", "month": 10, "day": 23},
    11: {"name": "さそり座", "month": 11, "day": 21},
    12: {"name": "いて座", "month": 12, "day": 21},
}

result_list = [value['name'] for value in base_dic.values() if len(value['name']) != 4]
print(result_list)

conste_list = []
for value in base_dic.values():
    if len(value['name']) != 4:
        conste_list.append(value['name'])
print(conste_list)
