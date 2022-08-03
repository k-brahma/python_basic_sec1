month_info_tuple = (
    (1, "Jan", "睦月", "むつき",),
    (2, "Feb", "如月", "きさらぎ",),
    (3, "Mar", "弥生", "やよい",),
    (4, "Apr", "卯月", "うづき",),
    (5, "May", "皐月", "さつき",),
    (6, "Jun", "水無月", "みなづき",),
    (7, "Jul", "文月", "ふみづき",),
    (8, "Aug", "葉月", "はづき",),
    (9, "Sep", "長月", "ながつき",),
    (10, "Oct", "神無月", "かんなづき",),
    (11, "Nov", "霜月", "しもつき",),
    (12, "Dec", "師走", "しわす",),
)

kana_list = []
for month_tuple in month_info_tuple:
    if len(month_tuple[3]) > 3:
        kana_list.append(month_tuple[3])
print(kana_list)

comp_list = [month_tuple[3] for month_tuple in month_info_tuple if len(month_tuple[3]) > 3]
print(comp_list)
