from manim import *
from manim.utils.paths import straight_path

class Stack(VGroup):
    def __init__(self, data, title="Stack", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data
        self.table_title = Text(title)
        self.update_table()
    
    @override_animation
    def interpolate(self, mobject1, mobject2, alpha, path_func=...):
        mobject1.set_opacity(alpha)
        mobject2.set_opacity(1-alpha)
        return self
    
    def get_table(self):
        return self.table

    def set(self, value):
        self.data.append(str(value))
        self.update_table()
    
    def unset(self):
        self.data.pop()
        self.update_table()
    

    def update_table(self):
        if (len(self.data) == 0):
            self.become(VGroup(self.table_title))
            return
        self.con_table = [[elem] for elem in self.data]
        self.table = Table(self.con_table, include_outer_lines=True)
        self.table_title.next_to(self.table, UP)
        self.become(VGroup(self.table, self.table_title))
    
    def push(self, value):
        return Stack(self.data + [value])
    
    def pop(self, **kwargs):
        return Stack(self.data[:-1])

class MyScene(Scene):
    def construct(self):
        s1 = Stack(data=["0x0134"])
        self.add(s1)
        s2 = s1.push("0x4321")
        self.play(FadeTransform(s1, s2))
        self.wait()
        s1 = s2.pop()
        self.play(FadeTransform(s2, s1))
        self.wait()