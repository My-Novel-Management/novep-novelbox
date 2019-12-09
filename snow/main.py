# -*- coding: utf-8 -*-
"""Main story.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from config import PERSONS, CHARAS, STAGES, DAYS, TIMES, ITEMS, WORDS
from snow.demo.demo import ep_demo


## main
def ch_main(w: World):
    return w.chapter("main",
            ep_demo(w),
            )

def world():
    """Create a world.
    """
    w = World("")
    w.set_db(PERSONS, CHARAS,
            STAGES, DAYS, TIMES,
            ITEMS,
            WORDS)
    return w

def story(w: World):
    return w.story("Sample",
            ch_main(w),
            )

def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

