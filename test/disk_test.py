from manim import *
import test_setup
from manim_datastructures import *

class theScene(Scene):
    def construct(self):
        disk1 = m_disk().to_edge(LEFT)
        disk2 = m_disk().to_edge(RIGHT)
        self.add(disk1, disk2)

        pol = disk1.color_between(disk2, BLUE, 0, 2, 2)

        self.add(pol)