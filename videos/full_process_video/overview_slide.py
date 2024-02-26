from manim import *
import setup
from manim_datastructures import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
from manim_voiceover.services.recorder import RecorderService
import os


class overview_slide(VoiceoverScene):

    def construct(self):

        self.set_speech_service(
            AzureService(
                voice="nb-NO-FinnNeural",
                style="default",
            )
        )
        # self.set_speech_service(RecorderService())


        # get the environment variable called LANG
        lang = os.environ.get("LANG", "nor")

        text = utils.get_text(f"text_to_speech/{lang}/overview_slide/1.txt")

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

        with self.voiceover(text=text) as tracker:
            self.play(Create(pointlist.scale(0.8)))
        self.wait()