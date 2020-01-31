# -*- coding: utf-8 -*-
"""Main story.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic, accessory
from config import PERSONS, AREAS, STAGES, DAYS, TIMES, ITEMS, WORDS, RUBIS, LAYERS
## local files
## blocks
## settings


## main
def ch_main(w: World):
    return w.chapter("main",
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
    w.setBaseDate(2010)
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

