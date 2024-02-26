from manim import *
import numpy as np
from .m_abstract_memory import m_abstract_memory

class m_memory(m_abstract_memory):
    
    def __init__(self, height=5, width=2, num_cells=4):
        super().__init__(height, width, num_cells)

        start = self.start + self.between

        for _ in range(num_cells):
            self.add(Line(start, (start + (RIGHT * width))))
            start += self.between
