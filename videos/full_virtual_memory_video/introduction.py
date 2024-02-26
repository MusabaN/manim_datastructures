from manim import *
import setup
from manim_datastructures import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
from manim_voiceover.services.recorder import RecorderService
import os


class Introduction(VoiceoverScene, MovingCameraScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="en-US-DavisNeural",
                style="friendly",
            )
        )

        # pcb loads into cr3 register on cpu
        pcb = m_table(
            title="PCB",
            data= {
                "PID": 1,
                "PC": 21,
                "BP": 0,
                "SP": 0,
                "PDIR": 539,
            },
        )

        lang = os.environ.get("LANG", "nor")

        text = utils.get_text(f"text_to_speech/{lang}/introduction/1.txt")
        
        with self.voiceover(text=text) as tracker:
            self.play(Create(pcb))
            self.wait()
            self.wait_until_bookmark("A")
            self.play(pcb.highlight_cell("PDIR"))
            self.wait()

        self.play(pcb.animate.rescale(0.7).to_edge(LEFT))
        self.wait()
        
        cpu = m_table(
            title="CPU",
            data={
                "BP": 12,
                "SP": 18,
                "PC": 43,
                "EAX": 435,
                "CR3": 896,
            }
        ).shift(RIGHT*0.5)

        text = utils.get_text(f"text_to_speech/{lang}/introduction/2.txt")

        with self.voiceover(text=text) as tracker:
            self.play(Create(cpu))

            self.wait()

            self.play(
                AnimationGroup(
                    cpu.animate.rescale(0.9).to_edge(RIGHT).shift(LEFT),
                    Wait(),
                    pcb.animate.rescale(0.9).to_edge(LEFT).shift(RIGHT),
                )
            )

            self.wait_until_bookmark("A")
            self.play(
                cpu.highlight_cell("CR3")
            )

            
            self.wait_until_bookmark('B')
            self.play(
                LaggedStart(
                    pcb.highlight_cell("PDIR"),
                    cpu.animate_change("CR3", pcb.data["PDIR"])
                )
            )

        self.wait()

        self.play(
            AnimationGroup(
                Uncreate(cpu),
                Uncreate(pcb),
            )
        )
        self.wait()