from manim import *
import test_setup
from manim_datastructures import *

class theScene(Scene):
        def construct(self):
            cpu1 = m_table(data= {
                "PC": 0,
                "BP": 1,
                "SP": 2,
                "EAX": 3,
            },
            scale=0.75).to_edge(LEFT + UP)
            self.add(cpu1)
            self.play(cpu1.animate_change("PC", 0x20, run_time=2, rate_func=linear))
            self.wait()
            self.play(cpu1.animate_change("EAX", 0x05, run_time=2, rate_func=linear))
            self.wait()
            self.play(cpu1.highlight_cell("EAX", run_time=2, rate_func=linear))
            self.wait()
            self.play(cpu1.animate.move_to(ORIGIN))
            self.wait()