from manim import *
import test_setup
from manim_datastructures import *

class theScene(Scene):
        def construct(self):
            m = m_memory(table=["Program 1","Program 2","Program 3"],number=5,).to_edge(UP)
            self.add(m)
                      
