from manim import *
import test_setup
from manim_datastructures import *

class theScene(Scene):
        def construct(self):
            m1 = m_memory(num_cells=10).to_edge(LEFT)
            m2 = m_memory(num_cells=10).to_edge(RIGHT)

            self.add(m1, m2)

            colored_area = m1.color_between(m2, BLUE, 0, 0, 3, direction=RIGHT)

            self.play(Create(colored_area), run_time=2)
            self.wait()

            colored_area2 = m2.color_between(m1, GREEN, -1, 8, 1, direction=LEFT)

            self.play(Create(colored_area2), run_time=1)
            self.wait(1)


            self.play(Uncreate(colored_area), Uncreate(colored_area2), run_time=1)

            self.wait()
            
            self.play(Uncreate(m1), Uncreate(m2), run_time=1)

            self.wait()