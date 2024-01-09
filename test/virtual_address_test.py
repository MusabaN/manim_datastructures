from manim import *
import test_setup
from manim_datastructures import *


class theScene(Scene):
    def construct(self):

        va = m_virtual_address([1, 2, 3, 4, 5])



        self.add(va)
        
        va.set_bracket_points(1, 4)
        
        self.play(va.animate.show_bracket())
        self.wait()

        self.play(va.animate.set_bracket_points(2, 3))
        self.wait()

        self.play(va.animate.hide_bracket())
        self.wait()


        