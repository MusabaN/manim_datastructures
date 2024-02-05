from manim import *
import setup
from manim_datastructures import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os

class ContextSwitch(VoiceoverScene, MovingCameraScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="nb-NO-FinnNeural",
                style="default",
            )
        )

        self.camera.frame.save_state()

        scene_title = Text("Context Switch", font_size=100)
        lang = os.environ.get("LANG", "nor")

        text = utils.get_text(f"text_to_speech/{lang}/context_switch/1.txt")

        with self.voiceover(text=text) as tracker:
            self.play(Write(scene_title))
            self.wait(tracker.duration - 3)
            self.play(FadeOut(scene_title))

        queue = m_queue([2, 3, 4], scale=0.8).to_edge(DOWN + LEFT)
        stack_1 = m_stack(scale=0.6).to_edge(RIGHT + UP)
        cpu = m_table(data= {
                "BP": 0,
                "SP": 0,
                "PC": 1,
                "EAX": 3,
            },
            title="CPU",
            scale=0.6).to_edge(UP)
        
        pcb_1 = m_table(
            title="PCB - 1",
            data= {
            "PID": 1,
            "PC": 21,
            "BP": 0,
            "SP": 0,
        },
        scale=0.6).to_edge(UP + LEFT)

        # animate camera move to right of cpu
        self.play(
            self.camera.frame.animate.scale(0.7).move_to(cpu.get_right() + (RIGHT / 2)),
        )

        text = utils.get_text(f"text_to_speech/{lang}/context_switch/2.txt")

        with self.voiceover(text=text) as _:
            self.play(Create(cpu))
            self.wait()
            self.play(Create(stack_1))
            self.wait()

        """
        Her ser vi at 
        """
        text = utils.get_text(f"text_to_speech/{lang}/context_switch/3.txt")
        with self.voiceover(text=text) as tracker:
            lst = [x for x in cpu.data.keys() if x not in ["SP", "BP"]]
            for key in lst:
                self.play(
                    LaggedStart(
                        cpu.highlight_cell(key, run_time=3),
                        stack_1.push(cpu.data[key], run_time=3),
                        *[Wait() for _ in range(7)],
                        cpu.animate_change("SP", cpu.data["SP"] + 1, run_time=3),
                        lag_ratio=0.25), run_time=((tracker.duration/len(lst))-(3/len(lst))))
                self.wait(3)

        text = utils.get_text(f"text_to_speech/{lang}/context_switch/4.txt")
        with self.voiceover(text=text) as tracker:
            # restore camera
            self.play(Restore(self.camera.frame))
            self.wait()

            self.play(Create(pcb_1), run_time=5)
            self.wait()

            # animate camera move to left of cpu
            self.play(
                self.camera.frame.animate.scale(0.7).move_to(cpu.get_left() + LEFT),
            )

        text = utils.get_text(f"text_to_speech/{lang}/context_switch/5.txt")
        with self.voiceover(text=text) as tracker:
            lst = ["BP", "SP"]
            for key in lst:
                self.play(
                    cpu.highlight_cell(key),
                    run_time=tracker.duration/2/len(lst)
                )
                self.play(
                    pcb_1.animate_change(key, cpu.data[key]),
                    run_time=tracker.duration/2/len(lst)
                )

        self.wait()

        text = utils.get_text(f"text_to_speech/{lang}/context_switch/6.txt")
        with self.voiceover(text=text) as tracker:
            # restore camera
            self.play(Restore(self.camera.frame))
            self.wait()

            self.play(Create(queue), run_time=5)
            self.wait()

            self.play(
                queue.enqueue(1, run_time=5, rate_func=linear),
                Uncreate(stack_1),
                Uncreate(pcb_1),
            )
            self.wait()
            self.play(
                queue.dequeue(run_time=5, rate_func=linear),
            )


        text = utils.get_text(f"text_to_speech/{lang}/context_switch/7.txt")
        with self.voiceover(text=text) as tracker:
            pcb_2 = m_table(data={
                "PID": 2,
                "PC": 21,
                "BP": 0,
                "SP": 4,
            },
                title="PCB - 2",
                scale=0.6).to_edge(UP + LEFT)

            stack_2 = m_stack(table=[4, 14, 67, 54], scale=0.6, sp_dynamic=False).to_edge(RIGHT + UP)

            self.play(
                Create(pcb_2),
                Create(stack_2),
                run_time=5)

            # move camera to left of cpu
            self.play(
                self.camera.frame.animate.scale(0.7).move_to(cpu.get_left() + LEFT),
            )

            for key in [x for x in pcb_2.data.keys() if x not in ["PID", "PC"]]:
                if key == "SP":
                    self.play(
                        LaggedStart(
                            pcb_2.highlight_cell(key, run_time=3),
                            cpu.animate_change(key, pcb_2.data[key], run_time=3),
                        )
                    )
                    self.wait()
                    # move camera right of cpu
                    self.play(
                        self.camera.frame.animate.move_to(cpu.get_right() + (RIGHT / 2)),
                    )
                    self.wait()
                    self.play(LaggedStart(stack_2.nudge_sp(pcb_2.data[key], run_time=3)))
                    self.wait()
                else:
                    self.play(
                        LaggedStart(
                            pcb_2.highlight_cell(key, run_time=3),
                            cpu.animate_change(key, pcb_2.data[key], run_time=3),
                        )
                    )

            self.wait()

            for key in ["EAX", "PC"]:
                value = stack_2.val_stack[-1]
                self.play(
                    stack_2.pop(),
                    cpu.animate_change(key, value, run_time=3),
                )
            self.play(Restore(self.camera.frame))
            self.wait()
