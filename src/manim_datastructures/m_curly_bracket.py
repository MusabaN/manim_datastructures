from manim import *
from .utils import *

class m_curly_bracket(VGroup):
    def __init__(self,height=None, width=None,**kwargs):
        super().__init__(**kwargs)
        svg_path = get_resource_path("resources/curly-bracket.svg")
        self.svg = SVGMobject(svg_path,height=height, width=width).set_color(WHITE)
        self.rect = SurroundingRectangle(self.svg)
        
        self.start = self.rect.get_corner(UL)
        self.end = self.rect.get_corner(UR)
        self.between = (self.end - self.start)/2

        self.add(self.svg)