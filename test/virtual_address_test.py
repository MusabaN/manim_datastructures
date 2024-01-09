from manim import *
import test_setup
from manim_datastructures import *

class theScene(Scene):
    def construct(self):

        va = m_virtual_address([1, 2, 3, 4, 5])

        self.add(va)
        
        self.play(va.animate.highlight(1, GREEN).popup_element(1))
        self.wait()

        self.play(va.animate.popdown_element(1).unhighlight(1))
        self.wait()

        