from manim import *
import setup
from manim_datastructures import *


class FirstScene(Scene):
    def construct(self):
        scene_title = Text("Context Switch", font_size=100)

        self.play(Write(scene_title))
        self.wait(3)
        self.play(FadeOut(scene_title))

        queue = m_queue([2, 3, 4], scale=0.8).to_edge(DOWN + LEFT)
        stack = m_stack(scale=0.6).to_edge(RIGHT + UP)
        cpu = m_table(data= {
                "BP": 0,
                "SP": 0,
                "PC": 1,
                "EAX": 3,
            }, 
            title="CPU",
            scale=0.6).to_edge(UP)
        
        pcb = m_table(data= {
            "PID": 47,
            "PC": 21,
            "BP": 0,
            "SP": 0,
        },
        title="PCB",
        scale=0.6).to_edge(UP + LEFT)
        
        self.play(Create(cpu), run_time=0.5)
        self.wait()
        self.play(Create(stack), run_time=0.5)
        self.wait()
        for key in [x for x in cpu.data.keys() if x not in ["SP", "BP"]]:
            self.play(
                LaggedStart(
                cpu.highlight_cell(key, run_time=3),
                stack.push(cpu.data[key], run_time=3),
                Wait(),
                Wait(),
                Wait(),
                Wait(),
                Wait(),
                Wait(),
                Wait(),
                cpu.animate_change("SP", cpu.data["SP"] + 1, run_time=3),
                lag_ratio=0.25))
            self.wait()
        
        self.play(Create(pcb), run_time=2)
        self.wait()

        for key in ["BP", "SP"]:
            self.play(
                LaggedStart(
                    cpu.highlight_cell(key, run_time=3),
                    Wait(),
                    Wait(),
                    Wait(),
                    Wait(),
                    Wait(),
                    Wait(),
                    Wait(),
                    Wait(),
                    pcb.animate_change(key, cpu.data[key], run_time=3),
                    lag_ratio=0.25,
                )
            )
            self.wait()

        



        self.play(Create(queue), run_time=2)
        self.wait()

        self.play(
            queue.enqueue(1, run_time=2, rate_func=linear),
        )
        self.wait()
        self.play(
            queue.dequeue(run_time=2, rate_func=linear),
        )

        self.wait()

