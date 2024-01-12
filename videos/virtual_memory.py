from manim import *
import setup
from manim_datastructures import *

class VirtualMemory(MovingCameraScene):
    def construct(self):

        scene_title = Text("Multi Level Paging", font_size=100)

        self.play(Write(scene_title))
        self.wait(2)
        self.play(FadeOut(scene_title))
        
        
        
        address = m_virtual_address([1,0,1,0,1,1,1,0,0,1,0,1]).to_edge(LEFT)
        ad_group = VGroup(address)

        self.play(FadeIn(address))
        
        self.play(address.animate.multi_popup(0,4).multi_highlight(0,4,GREEN))
        self.wait(0.5)
        self.play(address.animate.multi_popdown(0,4))
        self.wait(1)
        
        brace_outer = BraceBetweenPoints(address.get_coord(0,DL),address.get_coord(3,DR))
        self.play(FadeIn(brace_outer))
        outer_ad = Text("Outer address",font_size=35).next_to(brace_outer,DOWN,buff=0.1)
        self.play(FadeIn(outer_ad))  

        ad_group.add(brace_outer,outer_ad)  
        

        self.play(address.animate.multi_popup(4,8).multi_highlight(4,8,BLUE))
        self.wait(0.5)
        self.play(address.animate.multi_popdown(4,8))
        
        brace_inner = BraceBetweenPoints(address.get_coord(4,DL),address.get_coord(7,DR))
        self.play(FadeIn(brace_inner))
        inner_ad = Text("Inner address",font_size=35).next_to(brace_inner,DOWN,buff=0.1)
        self.play(FadeIn(inner_ad))

        ad_group.add(brace_inner,inner_ad)    

        
        self.play(address.animate.multi_popup(8,12).multi_highlight(8,12,YELLOW))
        self.wait(0.5)
        self.play(address.animate.multi_popdown(8,12))
        brace_offset = BraceBetweenPoints(address.get_coord(8,DL),address.get_coord(11,DR))
        self.play(FadeIn(brace_offset))
        offset = Text("Offset",font_size=35).next_to(brace_offset,DOWN,buff=0.1)
        self.play(FadeIn(offset))

        ad_group.add(brace_offset,offset)
        


        self.play(
            self.camera.frame.animate.scale(2).move_to(DOWN+RIGHT),
            ad_group.animate.move_to(UP*4+LEFT*5))

        
        #self.camera.frame.save_state()

        self.wait(1)
        pt = m_page_table(8,"Page table").move_to(DOWN*3)
        self.add(pt)
        self.wait(1)

        
        angled_1 = m_angled_arrow(start=outer_ad.get_bottom(),end=pt.get_coord(4,dir=LEFT),dir="y")
        self.play(FadeIn(angled_1))
        self.wait()
        
        pt2 = m_page_table(title="Page table").move_to(RIGHT*10+UP*1.5)
        self.add(pt2)
        self.wait(1)

        angled_2 = m_angled_arrow(start=pt.get_coord(4),end = pt2.get_bottom(),dir="x")
        self.play(FadeIn(angled_2))
        self.wait(2)

        angled_3 = m_angled_arrow(start=inner_ad.get_bottom(),end = pt2.get_coord(3,LEFT),dir="y")
        self.play(FadeIn(angled_3))
        self.wait(3)



