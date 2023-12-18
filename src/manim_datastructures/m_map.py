from manim import *
import numpy as np


class m_map(VGroup):
     def __init__(self, height=2, width=2, num_cells = 4):
        super().__init__()

        self.text = Text("Map")
        self.rect = Rectangle(height=height, width=width).surround(self.text, buff=2)
        self.num_cells = num_cells

        self.add(self.rect, self.text)