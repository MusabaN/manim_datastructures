from manim import *
import setup
from manim_datastructures import *


class paging(MovingCameraScene):
    def construct(self):
        memory = m_memory(height=5, width=2, num_cells=10).to_edge(LEFT)
        m = m_map(height=2, width=2, num_cells=10)
        ram = m_memory(height=3, width=2, num_cells=10).to_edge(UR).shift(DL/2)
        disk = m_disk(height=10, width=2, num_cells=10).to_edge(DR).shift(UL/2)

        self.play(Create(memory), Create(ram), Create(disk), Create(m))
        self.wait()


        pol_mem_map = memory.color_between(m, BLUE, 0, 2, 2)

        self.play(Write(pol_mem_map))
        self.wait()


        pol_map_ram = m.color_between(ram, BLUE, 0, 2, 2)

        self.add(pol_map_ram)

        pol_map_disk = m.color_between(disk, GREEN, 6, 3, 3)

        self.add(pol_map_disk)

