from manim import *
import setup
from manim_datastructures import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os


class process_waiting(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="nb-NO-FinnNeural",
                style="default",
            )
        )

        lang = os.environ.get("LANG", "nor")

        slide = VGroup(
            BulletedList(
                "For å få en prosess til å vente kan vi bruke systemkallet",
                r"Systemkallet \texttt{pid\_t wait(int *status)}",
                "Gjør at kallende prosess venter til hvilken som helst av barneprossene termineres (hvis det finnes noen)",
                "Dette returnerer:"
            ),
            BulletedList(
                r"\textbf{-1} Hvis ingen barneprosesser eksisterer",
                r"\textbf{PID} til den terminerte barneprosessen og legger statusen til prosessen i \textbf{status}",
                tex_environment="flushleft"
            )
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.7)

        slide[1].shift(RIGHT*0.5)


        text = utils.get_text(f"text_to_speech/{lang}/process_waiting_1.txt")
        with self.voiceover(text) as tracker:
            self.play(Create(slide))
        self.wait()
