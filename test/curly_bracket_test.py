from manim import *
import test_setup
from manim_datastructures import *

class TheScene(Scene):
    def construct(self):
        cb1 = m_curly_bracket()
        #cb2 = m_curly_bracket().to_edge(RIGHT)
        self.add(cb1)
        