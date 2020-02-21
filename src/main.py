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
            shin.be(),
            misa.be(),
            misa.do("二人でベッドに横たわっている"),
            misa.do("目覚めると、すぐそばに彼の微笑みがある"),
            _.do("髪を撫でられている"),
            shin.talk("おはよう、$misao"),
            misa.talk("なんか、照れる"),
            shin.talk("それはこちらも同じだよ",
                "でもこの気持ちを大切にしたいんだ"),
            misa.think("胸いっぱいに温もりが広がる"),
            misa.think("ずっと自分の性格がコンプレックスだった"),
            misa.explain("＜彼女の学生時代の暗い思い出＞"),
            misa.think("でも彼だけはこれを好きと言ってくれる"),
            shin.do("髪に埋もれて"),
            misa.talk("何してるの？"),
            shin.talk("今日のことを忘れないように", "匂いは記憶と結びついているんだ"),
            misa.talk("じゃあ、$meも"),
            misa.do("彼の胸板にじっとりと滲む汗に鼻頭をつけた"),
            ## NOTE
            ##  二人の紹介
            ##  ベッドで、髪を愛する男
            ##  自分に自信のない女
            ##  「運命」という言葉をやたらと口にする
            camera=w.misao,
            area=w.Tokyo,
            stage=w.on_lovehotel_int,
            day=w.in_happyday, time=w.at_morning,
            )

def sc_proposed(w: World):
    shin, misa = W(w.shin), W(w.misao)
    inside, outside = W(w.inside), W(w.outside)
    return w.scene("プロポーズ",
            shin.be(),
            misa.be(),
            shin.explain("二人で年越しカウントダウンライブにきている"),
            shin.think("彼女が楽しそうでほっとしている"),
            shin.explain("カウントダウンが始まる"),
            misa.talk("ねえ、$me、今本当に幸せなの。これ以上の幸せって、あるのかな？"),
            shin.talk("結婚しよう。そこが、$meたちのゴールだよ"),
            misa.talk("本当に？", "ねえ、本当？"),
            shin.talk("君はいつもそうやって確かめるね。答えは分かっているのに"),
            misa.talk("だって不安だから。今まで、あなたのような男性には出会えなかった。運命の神様に悪さされてたから"),
            shin.talk("これからはずっと、幸せだ"),
            shin.do("彼女の髪を撫でる"),
            misa.think("彼の優しさを感じた"),
            misa.talk("$meの人生を、もらって下さい"),
            shin.look("最高の笑顔"),
            outside.look("打ち上げ花火が上がり、新年を迎える"),
            ## NOTE
            ##  半年の付き合いを経て大晦日のカウントダウンライブ
            ##  結婚を遂に口にする男性
            stage=w.on_stadium,
            day=w.in_proposed, time=w.at_night,
            )

def sc_onthe_day(w: World):
    shin, misa = W(w.shin), W(w.misao)
    inside = W(w.inside)
    return w.scene("式当日",
            shin.be(),
            shin.do("式場の控室で、鏡に向かっている"),
            shin.do("鏡には綺麗に化粧された美しい髪の彼女"),
            shin.talk("やっと、君と一つになれる"),
            shin.do("彼の声を聞いて、微笑する"),
            shin.talk("さあ、行こうか"),
            shin.do("彼女は立ち上がり、控室から出る"),
            inside.look("＜何か不穏な様子が分かる、ものを置いておく＞"),
            ## NOTE
            ##  それから半年、六月がいいと式を迎える
            ##  ずっと彼女の独り言、のような思いの丈を綴る（しかし男しかいない）
            ##  ここで違和感を抱かせる
            camera=w.shin,
            stage=w.on_chapel_int,
            day=w.in_wedding, time=w.at_midmorning,
            )

def sc_eternal_love(w: World):
    shin, misa = W(w.shin), W(w.misao)
    poli, pri = W(w.police), W(w.priest)
    inside = W(w.inside)
    return w.scene("永遠の愛を誓おう",
            pri.be(),
            shin.come("入場してくる"),
            shin.do("歩いてくるが、一人だけ", "隣には誰もいない"),
            shin.look("真っ白なウェディングドレス姿", "その長い黒髪が揺れる"),
            inside.look("長椅子が並ぶ", "誰も座っていない"),
            inside.look("$priestだけが待ち構える"),
            shin.think("やっとこの日を迎えられた"),
            shin.do("歩いてきて、場所につく"),
            pri.talk("愛を誓いますか？"),
            shin.talk("はい、誓います"),
            shin.hear("その声は彼女のものではなく、彼自身のものだった"),
            poli.come("扉を開けて駆け込んでくる"),
            poli.talk("大人しくしろ、$full_shin！", "お前には$full_misao殺害容疑が掛かっている！"),
            shin.do("振り返った彼の顔、化粧され、微笑していた"),
            shin.talk("だって彼女、心はこの髪のように美しくはなかったんだもの"),
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

