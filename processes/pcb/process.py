from manim import *


def create_pcb(strings, numbers, scene):

    table_list = [[s, str(n)] for s, n in zip(strings, numbers)]

    table = Table(table_list)
    table.set_color(WHITE)

    table.scale(0.5)
    table.to_edge(LEFT)

    scene.play(table.create())


    return table



class tellMeWhy(Scene):
    def construct(self):
        hva_er_process = Text('What is a process?')
        hva_er_process.to_edge(UP)

        self.add(hva_er_process)

        pcb_group = create_pcb(["Instruction pointer", "Stack pointer", "Base pointer"], [0, 1, 2], self)
        self.wait(2)

        self.play(FadeOut(pcb_group))
        self.remove(pcb_group)
        self.wait(3)

