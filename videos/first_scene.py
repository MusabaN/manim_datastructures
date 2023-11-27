from manim import *
import setup
from manim_datastructures import *


class FirstScene(Scene):
    def construct(self):
        queue = m_queue([1, 2, 3], scale=0.8).to_edge(DOWN + LEFT)
        stack = m_stack([4, 5, 6], scale=0.6).to_edge(RIGHT + UP)
        cpu = m_table(data= {
                "PC": 0,
                "BP": 1,
                "SP": 2,
                "EAX": 3,
            }, 
            title="CPU",
            scale=0.6).to_edge(UP)
        
        pcb = m_table(data= {
            "PID": 0,
            "PC": 0,
            "BP": 1,
            "SP": 2,
        },
        title="PCB",
        scale=0.6).to_edge(UP + LEFT)
        
        
        
        self.add(queue, stack, cpu, pcb)

        self.play(
            queue.enqueue(4, run_time=2, rate_func=linear),
            stack.push(1, run_time=2, rate_func=linear),
            cpu.animate_change("PC", 0x20, run_time=2, rate_func=linear),
            pcb.animate_change("PC", 0x20, run_time=2, rate_func=linear),
        )
        self.wait()

