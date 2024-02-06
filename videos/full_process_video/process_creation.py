from manim import *
import setup
from manim_datastructures import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
from manim_voiceover.services.recorder import RecorderService

import os


#Notater for denne delen finnes i notes.md under Process creation

class process_creation(VoiceoverScene):

    def construct(self):
        # self.set_speech_service(
        #     AzureService(
        #         voice="nb-NO-FinnNeural",
        #         style="default",
        #     )
        # )
        self.set_speech_service(RecorderService())

        # get the environment variable called LANG
        lang = os.environ.get("LANG", "nor")

        example_code = VGroup(
            Text("main.py"),
            Code(
                file_name="code_examples/example1.py",
            )
        ).arrange(DOWN, aligned_edge=LEFT)
        
        """
        Dette er et eksempel på et program
        """
        text1 = utils.get_text(f"text_to_speech/{lang}/process_creation_1.txt")
        with self.voiceover(text=text1) as tracker:
            self.play(Create(example_code), run_time=tracker.duration)
        self.wait()

        """
        Eksekveringen av et program kaller vi prosess
        Ved kjøringen av et program får vi en del tilstandsinformasjon
        Som for eksempel prosess ID, pekere til minneområder, tilstand, signaler,
        pekere til stacken, osv
        Denne informasjonen må lagres, som også er en del av prosessen.
        Når programmet er skrevet, så kan vi kjøre det i terminalen, slik som i eksempelet her.
        """

        text2 = utils.get_text(f"text_to_speech/{lang}/process_creation_2.txt")
        with self.voiceover(text=text2) as tracker:
            self.play(example_code.animate.to_edge(UP), run_time=(tracker.duration/4))

        example_execution = VGroup(
            Text("terminal"),
            Code(file_name="code_examples/example1_output.txt", insert_line_no=False)
        ).arrange(DOWN, aligned_edge=LEFT)\
            .next_to(example_code, DOWN, aligned_edge=LEFT)

        text3 = utils.get_text(f"text_to_speech/{lang}/process_creation_3.txt")
        with self.voiceover(text=text3) as tracker:
            self.play(Create(example_execution), run_time=(tracker.duration/2))
        self.wait()




