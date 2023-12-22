from manim import *
import test_setup
from manim_datastructures import *

class TheScene(Scene):
    def construct(self):
        ad = m_address(numberseq=[1,0,1,0,1,1,1,0,0,1,0,1],scale=0.5)
        ad.highlight_cells_anim(1,3,BLUE)
        self.add(ad)
        self.wait(1)
        #self.play(Create(ad.highlight_cells(5,9,BLUE)))
        #self.wait(1)
        #self.remove(ad)
        #self.add(ad.highlight_cells(1,3,BLUE))
        self.play(ad.highlight_cells_anim(5,9))
        self.play(ad.highlight_cells_anim(1,2))
        