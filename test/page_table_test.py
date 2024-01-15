from manim import *
import test_setup
from manim_datastructures import *

class theScene(Scene):
    def construct(self):
        pt = m_page_table(scale=0.75, title="Inner page table",num_of_entries=8)
        self.add(pt)
        self.wait()