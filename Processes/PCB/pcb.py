from manim import *


class pcbMoving(Scene):
    def construct(self):
        rect = RoundedRectangle(corner_radius = 0.5,height = 6.0,width = 4.0)
        self.add(rect)
        text = Text("PCB").move_to(rect.get_center()).shift(UP,UP,LEFT)
        self.add(text)
        line = Line().set_length(4.0).shift(UP)
        self.add(line)
        desc = Text("Program counter \nStack \n     . \n     . \n     .",font_size=30).move_to(rect.get_center()).move_to(LEFT*0.4)
        self.add(desc)

class miniPCB(Scene):
    def construct(self):
        rect = RoundedRectangle(corner_radius = 0.5, height=2.0, width = 4.0).shift(UP*2)
        self.add(rect)
        text = Text("PCB").move_to(rect.get_center()).shift(LEFT)
        self.add(text)
        group = VGroup(rect,text)
        self.play(group.animate.move_to(0))

    
