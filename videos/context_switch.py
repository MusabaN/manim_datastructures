from manim import *
import setup
from manim_datastructures import *


class ContextSwitch(Scene):
    def construct(self):
        queue = m_queue([1, 2, 3], scale=0.8).to_edge(DOWN + LEFT)
        stack = m_stack([4, 5, 6], scale=0.8).to_edge(RIGHT + UP)
        table = m_table(data= {
                "PC": 0,
                "BP": 1,
                "SP": 2,
                "EAX": 3,
            }, scale=0.8).to_edge(LEFT + UP)

        self.add(queue, stack, table)
        self.wait(2)