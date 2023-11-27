from manim import *
import test_setup
from manim_datastructures import *

class theSchene(Scene):
    def construct(self):
        s1 = m_stack([12], scale=0.75).to_edge(UP)
        self.play(s1.fade_in())

        self.play(s1.push(10000))
        self.wait()

        self.play(s1.push(200))
        self.wait()

        self.play(s1.pop())
        self.wait()

        self.play(s1.fade_out())
        self.wait()

        self.play(s1.fade_in())
        self.wait()

        self.play(s1.pop())
        self.wait()

        self.play(s1.push(200))
        self.wait()

        self.play(s1.pop())
        self.wait()

        self.play(s1.pop())
        self.wait()

        self.play(s1.push(200))
        self.wait()

        self.play(s1.pop())
        self.wait()

