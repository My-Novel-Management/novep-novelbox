# -*- coding: utf-8 -*-
"""Story config.
"""


################################################################
#
# Sample:
#
# 1) PERSONS
#       人物簡易設定
# 2) CHARAS <- duplicated
# 2) STAGES
#       舞台基本設定
# 3) DAYS
#       年月日設定
# 4) TIMES
#       時間帯基本設定
# 5) ITEMS
#       小道具設定
# 6) WORDS
#       辞書設定
#
################################################################


PERSONS = (
        # Tag / 氏,名 / 歳 / 性別 / 職業 / 呼称 / 紹介
        ("yuki", "由季", "", 27, "female", "無職", "me:私"),
        ("sabu", "三郎", "", 35, "male", "猟師", "me:俺:yuki:由季さん"),
        ("masa", "正典", "", 38, "male", "猟師", "me:オレ"),
        )

CHARAS = (
        )

STAGES = (
        # Tag / 名前 / 紹介
        ("house", "三郎の山小屋"),
        )

DAYS = (
        # Tag / 名前 / 月 / 日 / 年
        ("dead", "山で亡くなった日", 12,27, 2008),
        ("athome", "家で目覚めた日", 12,30, 2008),
        ("memory", "思い出語り", 1,20, 2009),
        ("goout", "街に出かけた日", 2,20, 2009),
        ("find", "発見した日", 3,20, 2019),
        )

TIMES = (
        # Tag / 名前 / 時 / 分
        )

ITEMS = (
        # Tag / 名前 / 紹介
        )

WORDS = (
        # Tag / 名前 / 紹介
        )

