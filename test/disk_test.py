from manim import *
import test_setup
from manim_datastructures import *

class theScene(Scene):
    def construct(self):
        disk1 = m_disk()
        self.add(disk1)

        #pol = disk1.color_between(disk2, BLUE, 0, 0, 4)

        #self.add(pol)