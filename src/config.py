# -*- coding: utf-8 -*-
"""Story config.
"""

################################################################
#
# Sample:
#
# 1) PERSONS
#       人物簡易設定
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
# 7) RUBIS
#       ルビ設定
# 8) LAYERS
#       レイヤ設定
#
################################################################


PERSONS = (
        # Tag / 名前 / 氏,名 / 歳 / 誕生日 / 性別 / 職業 / 呼称 / 紹介
        ("shin", "慎一郎", "日陰,慎一郎", 30,(1,1), "male", "会社員", "me:俺"),
        ("misao", "操", "霜月,操", 30,(1,1), "female", "会社員", "me:私"),
        ## mob
        ("police", "刑事", "", 40,(1,1), "male", "刑事"),
        ("priest", "牧師", "", 50,(1,1), "male", "牧師"),
        )

AREAS = (
        # Tag / 名前 / x,y / 備考
        ("Shimane", "島根県", 13303,3528),
        )

STAGES = (
        # Tag / 名前 / 場所 / 紹介
        ("lovehotel", "ラブホテル", "Tokyo"),
        ("manshion", "マンション", "Tokyo"),
        ("stadium", "スタジアム", "Tokyo"),
        ("chapel", "チャペル", "Shimane", "離島にあるチャペル"),
        )

DAYS = (
        # Tag / 名前 / 月 / 日 / 年
        ("happyday", "幸せな日々", 10,10, 2019),
        ("proposed", "プロポーズした日", 12,31, 2019),
        ("wedding", "挙式当日", 6,4, 2020),
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

RUBIS = (
        # Base / Rubi / Exclusion / Type
        ("撫で", "｜撫《な》で"),
        ("安堵", "｜安堵《あんど》"),
        ("僅か", "｜僅《わず》か"),
        ("濡れ羽色", "｜濡《ぬ》れ｜羽色《ばいろ》"),
        ("嘲笑", "｜嘲笑《ちょうしょう》"),
        ("滲む", "｜滲《にじ》む"),
        ("纏った", "｜纏《まと》った"),
        ("踵", "｜踵《かかと》"),
        ("赤絨毯", "｜赤絨毯《あかじゅうたん》"),
        ("常套句", "｜常套句《じょうとうく》"),
        ## 人名
        ("操", "｜操《みさお》"),
        ("慎一郎", "｜慎一郎《しんいちろう》"),
        ("日陰慎一郎", "｜日陰慎一郎《ひかげしんいちろう》"),
        ("霜月操", "｜霜月操《しもつきみさお》"),
        )

LAYERS = (
        # Key / Title / Words
        )

