from manim import *
import setup
from manim_datastructures import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class overview_slide(VoiceoverScene):

    def construct(self):

        self.set_speech_service(
            AzureService(
                voice="nb-NO-FinnNeural",
                style="default",
            )
        )

        intro_text = utils.get_text("text_to_speech/nor/overview_slide.txt")

        pointlist = BulletedList(
            "Process",
            "Process creation",
            "Process creation - fork()",
            "Program execution",
            "Process waiting",
            "Process termination",
            "Process states",
            "Context switching",
        )

        with self.voiceover(text=intro_text) as tracker:
            self.play(Create(pointlist.scale(0.8)), run_time=tracker.duration)
        self.wait()