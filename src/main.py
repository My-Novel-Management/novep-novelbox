# -*- coding: utf-8 -*-
"""Main story.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer
from storybuilder.assets import basic, accessory
from config import PERSONS, AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS, LAYERS
## local files
## blocks
## settings


## Areas
W = Writer
_ = W.getWho()


## scenes
def sc_herhair_loved(w: World):
    shin, misa = W(w.shin), W(w.misao)
    return w.scene("髪を愛する男",
            ## NOTE
            ##  二人の紹介
            ##  ベッドで、髪を愛する男
            ##  自分に自信のない女
            ##  「運命」という言葉をやたらと口にする
            camera=w.shin,
            area=w.Tokyo,
            stage=w.on_lovehotel_int,
            day=w.in_happyday, time=w.at_morning,
            )

def sc_proposed(w: World):
    shin, misa = W(w.shin), W(w.misao)
    return w.scene("プロポーズ",
            ## NOTE
            ##  半年の付き合いを経て大晦日のカウントダウンライブ
            ##  結婚を遂に口にする男性
            stage=w.on_stadium,
            day=w.in_proposed, time=w.at_night,
            )

def sc_onthe_day(w: World):
    shin, misa = W(w.shin), W(w.misao)
    return w.scene("式当日",
            ## NOTE
            ##  それから半年、六月がいいと式を迎える
            ##  ずっと彼女の独り言、のような思いの丈を綴る（しかし男しかいない）
            ##  ここで違和感を抱かせる
            stage=w.on_chapel_int,
            day=w.in_wedding, time=w.at_midmorning,
            )

def sc_eternal_love(w: World):
    shin, misa = W(w.shin), W(w.misao)
    return w.scene("永遠の愛を誓おう",
            ## NOTE
            ##  一人だけで入場してくる
            ##  牧師以外誰もいない
            ##  神の前で愛を誓う
            ##  彼女の髪を着た、彼
            ##  そこに駆け込んでくる刑事
            )


## episodes
def ep_happydays(w: World):
    return w.episode("幸福な日々",
            ## NOTE
            ##  - 彼女の髪を愛する男
            ##  - その髪を守る為には命すら投げ捨てる
            ##  - プロポーズし、夢を語り合う
            sc_herhair_loved(w),
            sc_proposed(w),
            )

def ep_weddingbell(w: World):
    return w.episode("ウェディングベルを聴く日に",
            ## NOTE
            ##  - 式当日
            ##  - 友人は誰もいない。二人きりの挙式
            ##  - 牧師の前で誓う、永遠の愛を
            sc_onthe_day(w),
            sc_eternal_love(w),
            )

## main
def ch_main(w: World):
    return w.chapter("main",
            ## NOTE
            ##  - 結婚式以前
            ##  - 式当日
            ep_happydays(w),
            ep_weddingbell(w),
            )

def create_world():
    """Create a world.
    """
    w = World("黒髪")
    w.setCommonData()
    w.setAssets(basic.ASSET)
    w.setAssets(accessory.ASSET)
    w.buildDB(PERSONS,
            AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS,
            RUBIS, LAYERS)
    w.setBaseDate(2020)
    w.setBaseArea("Tokyo")
    # set persons
    # set stages
    # set block
    # set outline
    w.setOutline("彼が一番好きと言ってくれた長い黒髪を大切にしてきた女性は、ついにその彼と結婚式を迎える。だが")
    return w

def main(): # pragma: no cover
    w = create_world()
    return w.build(
            ch_main(w),
            )

if __name__ == '__main__':
    import sys
    sys.exit(main())

