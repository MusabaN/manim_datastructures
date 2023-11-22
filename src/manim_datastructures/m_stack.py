from manim import *

class m_stack(VGroup):
    def __init__(self, table=[], scale=1, title="Stack", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scale = scale
        self.top_line = Line(LEFT, RIGHT).scale(self.scale)
        self.title = Text(title).scale(self.scale).next_to(self.top_line, UP)
        self.bp = self.create_pointers([LEFT, RIGHT], "BP")
        self.sp = self.create_pointers([RIGHT, LEFT], "SP")
        self.stack = []
        self.prev = self.top_line

        self.add(self.title, self.top_line, self.bp, self.sp)
        for i in table:
            self.push_inner(i)
        
        if (len(table) > 0):
            self.sp.next_to(self.stack[-1], RIGHT)

    
    def create_textbox(self, string, font_size, color=WHITE):
        result = VGroup()
        text = Text(string, font_size=font_size)
        box = Rectangle(stroke_color=color).surround(text)
        box.width = 2
        result.add(box, text)
        return result.scale(self.scale)
        
    
    def create_pointers(self, direction, name):
        pointer = Arrow(start=direction[0], end=direction[1], stroke_width=3, buff=0.5).scale(self.scale, scale_tips=True).next_to(self.top_line, direction[0])
        text = Text(name, font_size=30).scale(self.scale).next_to(pointer, direction[0])
        return VGroup(pointer, text)
    
    def push_inner(self, value):
        new_elem = self.create_textbox(str(value), 30).next_to(self.prev, DOWN, buff=0)
        self.add(new_elem)
        self.stack.append(new_elem)
        self.prev = self.stack[-1]
        return new_elem
    
    def push(self, value, **kwargs):
        anims = []
        new_elem = self.push_inner(value)
        anims.append(FadeIn(new_elem, shift=UP))
        anims.append(self.sp.animate.next_to(new_elem, RIGHT))
        anims.append(Wait())
        return LaggedStart(*anims, 
            group=VGroup(new_elem, self.sp),
            **kwargs)
    
    def pop(self, **kwargs):
        if len(self.stack) == 0:
            return Succession(**kwargs)
        anims = []
        anims.append(FadeOut(self.stack[-1], shift=DOWN))
        anims.append(Wait())
        self.remove(self.stack.pop())
        if len(self.stack) > 0:
            anims.append(self.sp.animate.next_to(self.stack[-1], RIGHT))
            self.prev = self.stack[-1]
        else:
            anims.append(self.sp.animate.next_to(self.top_line, RIGHT))
            self.prev = self.top_line
        return LaggedStart(*anims, **kwargs)
    
    def fade_out(self, **kwargs):
        anims = []
        for elems in self:
            anims.append(FadeOut(elems))
        return AnimationGroup(*anims, **kwargs)
    
    def fade_in(self, **kwargs):
        anims = []
        for elems in self:
            anims.append(FadeIn(elems))
        return AnimationGroup(*anims, **kwargs)


if __name__ == "__main__":
    class theScene(Scene):
        def construct(self):
            s1 = m_stack([12], scale=0.75).to_edge(UP)
            self.play(s1.fade_in())

            self.play(s1.push(10000))
            self.wait()

            self.play(s1.push(200))
            self.wait()

            self.play(s1.pop())
            self.wait()

            self.play(s1.fade_out())
            self.wait()

            self.play(s1.fade_in())
            self.wait()

            self.play(s1.pop())
            self.wait()

            self.play(s1.push(200))
            self.wait()

            self.play(s1.pop())
            self.wait()

            self.play(s1.pop())
            self.wait()

            self.play(s1.push(200))
            self.wait()

            self.play(s1.pop())
            self.wait()
    import os
    os.system("manim -p -ql ./m_stack.py theScene")
    input("Press Enter to continue...")
    os.system("rm -rf ./__pycache__")
    os.system("rm -rf ./media")