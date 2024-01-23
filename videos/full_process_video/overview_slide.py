from manim import *
import setup
from manim_datastructures import *


class overview_slide(Scene):

    def construct(self):
        pointlist = BulletedList(
            "Process",
            "Process creation",
            "Process creation - fork()",
            "Program execution",
            "Process waiting",
            "Process termination",
            "Process states",
            "Context switching",
            "Process vs threads",
        )
        
        self.play(Create(pointlist.scale(0.8)))
        self.wait()