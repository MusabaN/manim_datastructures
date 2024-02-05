from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class AzureExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="nb-NO-FinnNeural",
                style="default",
            )
        )

        circle = Circle()
        square = Square().shift(2 * RIGHT)

        with self.voiceover(text="Denne sirkelen tegnes mens jeg snakker.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)

        with self.voiceover(text="La oss flytte den 2 enheter til venstre") as tracker:
            self.play(circle.animate.shift(2 * LEFT), run_time=tracker.duration)

        with self.voiceover(text="La oss gjøre den om til en firkant.") as tracker:
            self.play(Transform(circle, square), run_time=tracker.duration)

        with self.voiceover(
            text="Du kan også endre pitchen på stemmen sånn som dette.",
            prosody={"pitch": "+40Hz"},
        ) as tracker:
            pass

        with self.voiceover(text="Tusen takk for at du så på!"):
            self.play(Uncreate(circle))

        self.wait()