"""
利用可能な　ZoneInfo の一覧を取得します。
(実務で使うことはなかなかないですが...いちおう、参考までに)
"""

import zoneinfo

zone_info_set = zoneinfo.available_timezones()
type(zone_info_set)
print(zone_info_set)
