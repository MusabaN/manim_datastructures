from manim import *
import test_setup
from manim_datastructures import *


class theScene(Scene):
    def construct(self):

        va = m_virtual_address([1, 2, 3, 4, 5])

        self.add(va)

        self.play(va.animate.multi_popup(1, 4).multi_highlight(1, 4, GREEN))
        self.wait()
        self.play(va.animate.multi_popdown(1, 4).multi_unhighlight(1, 4))
        self.wait()

        self.play(va.animate.multi_popup(1, 4).multi_highlight(1, 4, GREEN))
        self.wait()
        self.play(va.animate.multi_popdown(1, 4).multi_unhighlight(1, 4))
        self.wait()
        

        