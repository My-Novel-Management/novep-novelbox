# -*- coding: utf-8 -*-
"""Episode: start and end
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

W = Writer


## scenes
def sc_atohome(w: World):
    yu, sa = W(w.yuki), W(w.sabu)
    return w.scene("ささやかな家庭", "小さいが二人には満足がいく暮らしぶりだった",
            sa.awake(),
            yu.talk("あら？　起きられました？"),
            sa.look("既にできあがったスープがある。湯気が出ている"),
            yu.talk("どうぞ"),
            sa.look("だが$n_yukiのものは湯気がないのを"),
            yu.talk("$meは苦手ですから"),
            sa.feel("彼女の控えめなところに幸せを"),
            )

def sc_memories(w: World):
    yu, sa = W(w.yuki), W(w.sabu)
    return w.scene("思い出", "何故か出会いの頃のことがはっきり思い出せない",
            sa.talk("そういえば出会った頃のことをよく思い出せないな"),
            yu.talk("何言ってるんですか。あなたが山で助けてくれたんですよ？"),
            yu.talk("$meが足を痛めて困っていたところに、猟をしていたあなたが通りかかって"),
            sa.talk("そうだったかな？"),
            sa.talk("弁当ありがとう。ではいってくるよ"),
            yu.talk("いってらっしゃい、あなた"),
            sa.go(),
            yu.look(doing="見送る"),
            )

def sc_comespring(w: World):
    yu, sa = W(w.yuki), W(w.sabu)
    return w.scene("春が来る前に", "男は春が来る前にどうしても彼女にプレゼントしたかった",
            sa.talk("どうして止めるんだ？"),
            yu.talk("どうしても、町に降りなければなりませんか？"),
            sa.talk("春が近いというので、どうしてもお前に食べさせてやりたいのだ"),
            sa.think("銘菓の桜餅を"),
            yu.talk("いいですよ。$meはあなたがいるだけで充分なんですから"),
            sa.talk("とは言ってもな。お前の体のことを考えたら春になれば一度山を降りて"),
            sa.look("大きくなったお腹を"),
            yu.talk("他には何もいりません。今だけあればいいと、思いませんか？"),
            sa.be("無言で"),
            w.br(),
            sa.awake("夜半に"),
            sa.go(),
            yu.look(doing="悲しげに見送る"),
            sa.look("突然の猛吹雪を"),
            sa.remember("自分が死んだ時のことを"),
            )

def sc_truth(w: World):
    yu, sa = W(w.yuki), W(w.sabu)
    masa = W(w.masa)
    return w.scene("真実の姿", "真実は悲しいものだった",
            masa.come("家の中に"),
            masa.do("扉をぶち壊して"),
            masa.look("中を"),
            masa.look("仰向けで寝ている$n_sabu"),
            masa.talk("おい！"),
            masa.do("触れる"),
            masa.feel("冷たいと"),
            masa.consider("死んでいると"),
            )

## episode
def ep_hascomespring(w: World):
    return w.episode("春が来る", "まもなく春が来る、と彼女は言った",
            sc_atohome(w),
            sc_memories(w),
            sc_comespring(w),
            sc_truth(w),
            )

