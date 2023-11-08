from manim import *


class pcbMoving(Scene):
    def construct(self):
        large_group = largePCB()
        self.add(large_group)
        small_group = smallPCB().shift(2*UP)
        self.wait(0.5)
        self.play(TransformMatchingShapes(large_group,small_group))
        self.wait(0.5)      
        self.play(small_group.animate.move_to(0))
        self.wait(2.0)
        long_group = longPCB()

        self.play(TransformMatchingShapes(small_group, long_group))
        self.wait(2.0)

        self.play(TransformMatchingShapes(long_group, large_group))


def longPCB():
    long_rect = RoundedRectangle(corner_radius=0.5, height=2.0, width=8.0)
    long_text = Text("Process Control Block").move_to(
        long_rect.get_center())
    long_group = VGroup(long_rect, long_text)
    return long_group

def smallPCB():
    smaller_rect = RoundedRectangle(
        corner_radius=0.5, height=2.0, width=4.0)
    smaller_text = text = Text("PCB").move_to(
        smaller_rect.get_center()).shift(LEFT)
    small_group = VGroup(smaller_rect,smaller_text)
    return small_group

def largePCB():
    rect = RoundedRectangle(corner_radius=0.5, height=6.0, width=4.0)
    text = Text("PCB").move_to(rect.get_center()).shift(UP,UP,LEFT)
    line = Line().set_length(4.0).shift(UP)
    desc = Text("Program counter \nStack \n     . \n     . \n     .",
                font_size=30).move_to(rect.get_center()).move_to(LEFT*0.4)
    large_group = VGroup(rect,text,line,desc)
    return large_group
    
