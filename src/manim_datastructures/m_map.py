from manim import *
import numpy as np
from .m_abstract_memory import m_abstract_memory


class m_map(m_abstract_memory):
    def __init__(self, height=2, width=2, num_cells = 4):
        super().__init__(height, width, num_cells)

        self.text = Text("Map")
        self.rect.surround(self.text, buff=2)
        self.num_cells = num_cells

        self.start = self.rect.get_corner(UL)
        self.end = self.rect.get_corner(DL)

        self.between = (self.end - self.start) / self.num_cells

        self.add(self.text)