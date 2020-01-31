# -*- coding: utf-8 -*-
"""Demo story.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.builder.writer import Writer

W = Writer


## scenes
def sc_dontgoout(w: World):
    yu, sa = W(w.yuki), W(w.sabu)
    masa = W(w.masa)
    return w.scene("行かないで下さい", "彼女は何故か三郎が町に降りるのを止めた",
            yu.talk("お願いですから"),
            yu.do("引っ張る"),
            sa.talk("何故だ？　最近妙だぞ"),
            yu.talk("春が、近いのです"),
            sa.talk("だから春になれば山を降りて色々なところにお前を連れて行ってやりたい"),
            yu.refuse(),
            sa.talk("何故だ？"),
            sa.go("外に出て"),
            yu.tears(),
            w.br(),
            masa.come(),
            masa.look("冷たくなった$n_sabuを"),
            masa.feel("冷たいと"),
            masa.look(doing="まるで生きているように綺麗な肌をして笑っていた"),
            )

## episode
def ep_demo(w: World):
    return w.episode("Demo", "demo story",
            sc_dontgoout(w),
            )

