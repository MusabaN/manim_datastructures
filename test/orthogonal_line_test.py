from manim import *
import test_setup
from manim_datastructures import *

class theScene(Scene):
    def construct(self):
        r1 = Rectangle(height=6, width=3)
        r2 = Rectangle(height=5, width=2)
        VGroup(r1, r2).arrange(RIGHT, buff=3)
        self.add(r1, r2)
        l1 = m_orthogonal_line(r1.get_right(), r2, 
                path=((r2.get_top()+UP, "-|-"), 
                      (r2.get_top(), "|")),
                color=YELLOW
        )
        l1.add(l1.create_tip())
        l2 = m_orthogonal_line(r1.get_bottom(), r2,
                path=((r2.get_critical_point(DR) + DR, "|-"),
                      (r2.get_critical_point(RIGHT), "|-")),
                color=BLUE
        )
        l2.add(l2.create_tip())

        # It is backwards compatible
        l3 = m_orthogonal_line(r1.point_from_proportion(0.8),
                            r2.point_from_proportion(.4),
                            "-|-", color=GREEN)
        l3.add(l3.create_tip())
        self.add(l1, l2, l3)