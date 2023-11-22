from manim import *


class Stack2(VGroup):
    def __init__(self, title="Stack", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.line = Line(LEFT, RIGHT)

        self.sp_arrow = Arrow(start=RIGHT, end=LEFT, stroke_width=3, buff=0.5).next_to(self.line, RIGHT)
        self.sp_text = Text("SP", font_size=30).next_to(self.sp_arrow, RIGHT)
        self.sp = VGroup(self.sp_arrow, self.sp_text)

        self.bp_arrow = Arrow(start=LEFT, end=RIGHT, stroke_width=3, buff=0.5).next_to(self.line, LEFT)
        self.bp_text = Text("BP", font_size=30).next_to(self.bp_arrow, UP)
        self.bp = VGroup(self.bp_arrow, self.bp_text)

        self.prev = self.line



        self.stack = []

        self.update_stack()
    
    def update_stack(self):
        self.become(VGroup(self.line, 
                           self.sp, 
                           self.sp_text,
                           self.bp,
                           self.bp_text, 
                           *self.stack))

    def push(self, value, **kwargs):
        anims = []
        new_elem = (Text(str(value), font_size=30)).next_to(self.prev, DOWN)
        anims.append(Create(new_elem))
        anims.append(self.sp.animate.next_to(new_elem, RIGHT))
        anims.append(Wait())
        self.stack.append(new_elem)
        self.prev = self.stack[-1]
        self.become(VGroup(self.line, 
                           self.sp, 
                           self.sp_text,
                           self.bp,
                           self.bp_text, 
                           *self.stack))
        
        return Succession(*anims, **kwargs)

    def pop(self, **kwargs):
        anims = []
        anims.append(Uncreate(self.stack[-1]))
        anims.append(Wait())
        self.stack.pop()
        if len(self.stack) > 0:
            anims.append(self.sp.animate.next_to(self.stack[-1], RIGHT))
        else:
            anims.append(self.sp.animate.next_to(self.line, RIGHT))
        return Succession(*anims, **kwargs)
    

class MyScene(Scene):
    def construct(self):
        s1 = Stack2()
        self.add(s1)
        self.wait()
        self.play(s1.push(0x20))
        self.play(s1.push(0x30))
        self.play(s1.pop())
        self.play(s1.pop())
        self.wait()