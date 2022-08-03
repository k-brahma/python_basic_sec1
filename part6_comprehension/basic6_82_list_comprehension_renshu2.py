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

kan_list = []
for month_info in month_info_tuple:
    kan_list.append(month_info[2])
print(kan_list)

naiho_list = [month_info[2] for month_info in month_info_tuple]
print(naiho_list)
