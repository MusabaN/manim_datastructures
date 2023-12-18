from manim import *
import test_setup
from manim_datastructures import *

class theScene(Scene):
    def construct(self):
        map = m_map()
        self.add(map)