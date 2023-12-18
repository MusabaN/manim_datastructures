from manim import *
import test_setup
from manim_datastructures import *

class theScene(Scene):
    def construct(self):
        map = m_map().to_edge(RIGHT)
        self.add(map)
        mem = m_memory().to_edge(LEFT)
        self.add(mem)

        pol = mem.color_between(map, BLUE, 0, 0, 4)

        self.add(pol)
        