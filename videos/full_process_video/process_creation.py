from manim import *
import setup
from manim_datastructures import *


class process_creation(Scene):

    def construct(self):
        example_code = Code(
            file_name="example1.c",
        )
        self.play(Create(example_code))
        self.wait()

        back_rec = BackgroundRectangle(example_code.code[0:6], fill_opacity=0.2, color=GREEN)

        self.play(Create(back_rec))
        self.wait()

        self.play(Uncreate(back_rec))
        self.wait()


