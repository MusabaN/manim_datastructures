from manim import *
import setup
from manim_datastructures import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
from manim_voiceover.services.recorder import RecorderService
import os


class process_termination(VoiceoverScene):
    def construct(self):
        # self.set_speech_service(
        #     AzureService(
        #         voice="nb-NO-FinnNeural",
        #         style="default",
        #     )
        # )
        self.set_speech_service(RecorderService())
        lang = os.environ.get("LANG", "nor")

        slide = VGroup(
            Text("En prosess kan avsluttes på flere forskjellige måter:"),
            BulletedList(
                "Ingen flere instruksjoner å utføre i programmet - ukjent statusverdi",
                "En funksjon i et program avslutter med en retur - parameter for å returnere statusverdien",
                r"Systemkallet \texttt{void exit(int status)} - avslutter en prosess og returnerer statusverdien (se man 3 exit)",
                r"Systemkallet \texttt{int kill(pid\_t pid, int sig)} - sender et signal for å avslutte en prosess (se man 2 kill, man 7 signal)",
            ),
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.7)


        text = utils.get_text(f"text_to_speech/{lang}/process_termination/1.txt")
        with self.voiceover(text) as tracker:
            self.play(Create(slide))

        self.wait()
