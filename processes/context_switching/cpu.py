
from manim import *

def createCpu():
    cpu = Rectangle(height=2, width=4)
    cpu.set_color(WHITE)
    cpu.set_fill(color=WHITE, opacity=1)

    cpu_text = Text('CPU')
    cpu_text.next_to(cpu, UP)

    cpu_group = Group(cpu, cpu_text)

    return cpu_group



class MyScene(Scene):
    def construct(self):
        cpu = createCpu()
        self.add(cpu)
        self.wait(2)