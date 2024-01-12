from manim import *
from .m_abstract_memory import m_abstract_memory
from .utils import *

class m_disk(m_abstract_memory):
    def __init__(self, height=5, width=2, num_cells=4):
        super().__init__(height, width, num_cells)
        svg_path = get_resource_path("resources/disk.svg")
        self.svg = SVGMobject(svg_path).set_color(WHITE)
        self.rect.surround(self.svg, buff=0, stretch=True)
        self.num_cells = num_cells

        self.start = self.rect.get_corner(UL)
        self.end = self.rect.get_corner(DL)

        self.between = (self.end - self.start) / self.num_cells

        self.add(self.svg)