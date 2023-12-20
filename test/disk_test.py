from manim import *
import test_setup
from manim_datastructures import *

class theScene(Scene):
    def construct(self):
        disk1 = m_disk()
        self.play(Create(disk1))
        self.wait(3)

        #pol = disk1.color_between(disk2, BLUE, 0, 0, 4)

        #self.add(pol)