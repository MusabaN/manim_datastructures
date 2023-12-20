from manim import *


class the_scene(Scene):
    def construct(self):
        rect = Rectangle(width=100, height=100, color=BLUE, fill_opacity=1)
        svg = SVGMobject("/Users/oleskole/repos/manim_datastructures/test/disk.svg", stroke_color=WHITE, color=WHITE)

        self.add(rect, svg)