from manim import *


def create_pcb(color, strings):
    

    text_group = VGroup(*[Text(s) for s in strings])
    text_group.arrange(DOWN, aligned_edge=LEFT)
    rect = SurroundingRectangle(text_group, buff=0.1)

    result = VGroup(text_group, rect)

    return result

def create_pcb2(strings, numbers):

    left_column = VGroup(*[Text(s) for s in strings]).arrange(DOWN, aligned_edge=LEFT)
    right_column = VGroup(*[DecimalNumber(n) for n in numbers]).arrange(DOWN)

    columns = VGroup(left_column, right_column).arrange(RIGHT)

    rect = SurroundingRectangle(columns, buff=0.1)

    result = VGroup(columns, rect)


    return result



class tellMeWhy(Scene):
    def construct(self):
        hva_er_process = Text('What is a process?')
        hva_er_process.to_edge(UP)

        self.add(hva_er_process)

        pcb_group = create_pcb2(["Instruction pointer:", "Stack pointer:", "Base pointer:"], [0, 1, 2])

        self.add(pcb_group)
        self.wait(10)
