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
    inside = W(w.inside)
    return w.scene("髪を愛する男",
            shin.be(),
            misa.be(),
            w.comment("操視点で男の造形、顔や体つき、優しい雰囲気を与えるように"),
            misa.do("黒くて長い髪の毛が$Sの汗ばんだ背中に貼り付いていた",
                "それを優しく男の手が撫でる"),
            misa.wear("腰まである長い黒髪"),
            shin.talk("ごめん。起こしてしまったようだね"),
            misa.talk("ううん。いいの", "だって今、すごく幸福だから"),
            misa.do("間接照明で淡くピンクに照らされた部屋の、巨大なベッドの上で、二人は再びキスをした",
                "その影が天井へと映し出されて、二人で見上げて笑い、もう一度口づける"),
            misa.think("それは$Sにとって初めてのラブホテルという空間で、",
                "恐れていたものが彼とならちゃんと乗り越えられたという安堵と僅かに残る痛み、それ以上の幸福感に満たされ、今、このまま彼の中に溶けてしまいたいという思いだった"),
            w.comment("慎一郎の声の描写、彼女は彼の声と雰囲気が好き"),
            w.comment("男は執拗に彼女の髪を愛する／その触感などを言葉で"),
            shin.wear("がっしりした肩幅（学生時代に水泳を）"),
            w.comment("二人の付き合いの期間と、これから結婚するんだなという空気感"),
            w.comment("操の暗い学生時代。特に髪の毛がコンプレックスだったことの、具体的エピソード"),
            misa.do("彼の手はずっと$Sの髪を撫でている",
                "彼、$shinは出会った時から彼女の髪を好いてくれた",
                "腰まで真っ直ぐに伸びたそれは小さい頃から$Sの性格も相まって、他人から嘲笑の的になっていた",
                "でもそれを、彼は愛してくれたのだ"),
            shin.do("$Sは$CSの髪の毛を両手で掴み、そこに顔を埋める"),
            misa.talk("恥ずかしいって"),
            shin.talk("裸を見られるより？"),
            misa.think("確かに二人とも一糸まとわぬ姿でこれより恥ずかしいことがあるのだろうか、",
                "と一瞬考え込んだけれど、それでもやはり、自分の一部である髪の毛に大切な人が埋もれ、その匂いを嗅いでいる姿は何とも羞恥心を刺激する"),
            misa.talk("やっぱり恥ずかしいよ"),
            shin.talk("それでいい。今日のことを忘れないように、そういう気持ちを刻みつけておくんだ",
                "それにね、匂いは記憶ととてもよく結びつく",
                "$meはこれでもう、君を忘れない"),
            misa.talk("じゃあ、$meも"),
            misa.do("$Sはじっとり汗が滲む彼の大きな胸板に肌を寄せ、鼻頭をつけ、その香りを刻みつけた"),
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
            misa.explain("今年最後の歌が終わり、歓声が上がる中、スポットライトで照らされたステージ上に参加した全てのアーティストが現れる",
                "それを見ながら$Sは彼の手が自分の髪に触れているのを感じていた"),
            shin.talk("どうしたんだい？"),
            misa.explain("ステージ上に設置された巨大なスクリーンには年越しまでのリミットを数えるカウントダウンの数字が浮かび上がり、一つずつ、減っていく"),
            misa.talk("ううん。ただ漠然と幸福を感じただけ"),
            shin.do("彼は一瞬考え込み、それから湧き続ける歓声から隠すように$CSの右耳に口を寄せると、こう言った"),
            shin.talk("幸福はいつも漠然だよ", "ただそれは君が傍にいるからだ"),
            shin.wear("＜服装＞"),
            misa.wear("＜冬服だが、髪は強調しておく＞"),
            misa.do("彼の手がするすると滑るように$Sの髪を抜けていく",
                "それが心地良い",
                "まるで髪の毛一本一本に心が宿ったみたいに、彼のその指を待ち構えている",
                "これがきっと好きの先にある感情なのだと、$Sは最近思うのだ",
                "自分がずっと探していた、求めていた、愛、と呼ぶべきものだと"),
            shin.do("$Sは舞台上のアーティストが肩を組みながらカウントダウンコールをしているのを、楽しげに眺めている","&"),
            misa.do("その横顔の隙きのなさにうっとりとし、$Sはダウンジャケットの上から彼の肩に頬を寄せた"),
            misa.talk("ねえ、$me、今本当に幸福なの",
                "でもね、これ以上の幸福って、もうないんじゃないかって思えて、時々怖くなる"),
            shin.talk("$misaoはいつも何かに怯えているね",
                "こんなに素敵なものを持っているのに、自分が本当に綺麗なことに気づかず、暗い小屋に閉じこもろうとする",
                "それはね、罪だ", "$meに対しての"),
            misa.talk("罪？"),
            shin.talk("ああ", "だから君には罰を与えなければいけない"),
            misa.think("不意に彼が分からないことを言う",
                "最初は自分の理解力が足りないだけだと思っていたけれど、それが時折、ミステリアスを超えて恐怖の顔を覗かせることもある",
                "でもその先に決して自分を傷つけるナイフを手にしていない安心感もあり、今ではそういう彼特有の表現なのだと思えるようになっていた"),
            misa.talk("その罰は、何？"),
            misa.explain("カウントダウンの数字がどんどん小さくなる"),
            misa.do("それに伴い、彼の顔が近づいていく"),
            misa.do("心臓は高まり、陶磁器みたいな彼の顔が、唇が、優しくその罰を告げた"),
            shin.talk("結婚しよう", "君は$meと一緒になるんだ"),
            shin.do("彼の指が、$misaoの髪を撫でた"),
            misa.talk("$meの人生を、もらって下さい"),
            outside.look("会場では新年を告げる花火が打ち上がり、誰もがハッピーニューイヤーと声を上げた"),
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
            shin.explain("$misaoがどうしても式は六月が良い、と譲らなかったので、半年を待っての挙式となった"),
            shin.do("緊張気味に白一色のウェディングドレスに身を包み、今一度、控室の大きな鏡で彼を待つ自分の表情を確認する", "&"),
            shin.do("化粧で少し大きく見えるように誤魔化した目元には不安と期待が入り交ざった色が滲み、いつも以上に青白い顔で控え目に塗った紅だけが鮮血のようだ", "&"),
            shin.do("それでも口角を上げて笑みを作ってみる",
                "そうすることで今自分が幸福というベールを被ろうとしているのだと思い込む"),
            inside.look("化粧台の端には一輪だけ差された薔薇が、静かに$misaoたちのことを祝ってくれている"),
            w.comment("鏡に写すことで勘違いさせる"),
            w.comment("二人で会話しているような空気をもたせる"),
            shin.hear("と、ドアが開けられる音が聞こえ、続いて優しい声が掛けられた"),
            shin.talk("$misao、もう準備は良いかい？"),
            shin.do("はい、と力強く返事をし、立ち上がる",
                "まだベールの付いていない自分の髪が腰まで落ちる",
                "濡れ羽色、と彼が褒めてくれた手入れの行き届いたその髪も今日、一緒に彼のものとなる"),
            shin.do("彼の手がそれに触れる",
                "すっと指が髪を抜けていく"),
            shin.talk("今日も、綺麗だ",
                "いや、いつも以上に、綺麗だよ"),
            shin.talk("照れます"),
            shin.do("その彼の右手を掴み、控室を出る",
                "廊下には静かなピアノのメロディが流れていた"),
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
            shin.come("スタッフにドアが開けられ、式場が視界に広がる"),
            inside.look("宣誓台の前に立つ漆黒のローブを纏った白人の牧師以外、そのチャペルには誰の姿もなかった","&"),
            shin.think("これは二人で相談して決めたことだ",
                "本当にこの誓いを神聖なものにするなら邪魔な人間は一人も入れない方が良いと",
                "だから今、この場内は静まり返り、一歩、踏み出した自分の足音だけが響いた"),
            shin.do("細いヒールの踵が赤絨毯を踏みつける",
                "小さな花で飾られたそれはドレスの長い裾に隠れていたけれど、一歩踏み出す度にそっと顔を出す",
                "そのデザインが気に入っていた"),
            shin.think("拍手もなく、冷やかしの声も上がらない",
                "ただ静寂の中で行われるそれは、二人の儀式だった"),
            shin.do("ただ、本来なら自分を待つ白のタキシードがそこにはいない",
                "牧師だけが立つその場所まで、付き添いもなく、一人で辿り着くと、事情を知る金色の髭の彼は小さく頷いてくれた"),
            pri.talk("$misaoさん"),
            shin.do("そう呼びかけ、彼はお決まりの宣誓文を読み上げる"),
            shin.think("病めるときも健やかなるときも、富めるときも貧しいときも、という言葉が響いていく"),
            pri.talk("愛することを誓いますか？"),
            shin.do("ずっと待ち続けたその問いに、少し間を置いて、"),
            shin.talk("はい。誓います"),
            shin.do("と答えた"),
            pri.do("けれどそれを耳にした牧師は聖書を手にしたまま、目を広げて後ずさる","&"),
            shin.do("｜彼の声が《・・・・》｜男性のそれ《・・・・・》だったからだ"),
            poli.come("その時だった",
                "扉が勢い良く開けられ、複数の制服警官とスーツの刑事が雪崩込んでくる"),
            poli.talk("大人しくしろ、$full_shin！", "お前には$full_misao殺害容疑が掛かっている！"),
            shin.do("その呼びかけに答えるように微笑を浮かべて振り返った彼の頭からベールが取れ、その長い髪が揺れた",
                "その髪の毛を指に絡め、",
                "紅を引いた$full_shinの唇がゆっくりと動く"),
            shin.talk("だって彼女、心はこの髪のようには美しくなかったんだもの"),
            shin.do("そう答え、彼は愛おしむように手にした髪を口元まで持っていき、優しい口づけをした"),
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

