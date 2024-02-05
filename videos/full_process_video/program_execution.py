from manim import *
import setup
from manim_datastructures import *
from manim.mobject.text.text_mobject import remove_invisible_chars
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os


class program_execution(VoiceoverScene):

    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="nb-NO-FinnNeural",
                style="default",
            )
        )

        macode = utils.create_code(
                "code_examples/example3.c",
            )

        example_code = VGroup(
            Text("main.c"),
            remove_invisible_chars(macode)
        ).arrange(DOWN, aligned_edge=LEFT)\
            .scale(0.5)


        lang = os.getenv("LANG", "nor")

        text = utils.get_text(f"text_to_speech/{lang}/program_execution_1.txt")

        with self.voiceover(text) as tracker:
            self.play(Create(example_code))


        # highlight line number 15
        highlight = BackgroundRectangle(macode.code[14], color=GREEN, fill_opacity=0.2)\
                        .stretch_to_fit_width(macode.width).align_to(macode, LEFT)


        text = utils.get_text(f"text_to_speech/{lang}/program_execution_2.txt")
        with self.voiceover(text) as tracker:
            self.play(
                Succession(
                    Create(highlight),
                    Uncreate(highlight)
                ),
                run_time=tracker.duration
            )

        self.wait()

        self.play(example_code.animate.to_edge(LEFT))
        self.wait()

        slide = VGroup(
            BulletedList(
                "For å eksekvere et program kan man bruke blant annet execve()",
                r"int execve(const char *filename, char *const argv[], char *const envp[]);",
                "Det kjører programmet pekt på av filename, og sender med argumentene i argv og i miljøet gitt av envp.",
                r"Returnerer:",
                tex_environment="flushleft"
            ),

            # Create an indented sub-list for the return values
            BulletedList(
                r"\textbf{ingen retur verdi} på suksess, da bytter man bare til den nye prosessen",
                r"\textbf{-1} ved feil",
                tex_environment="flushleft"
            )
        ).arrange(DOWN, aligned_edge=LEFT)\
            .scale(0.4)\
            .next_to(example_code, RIGHT)

        # Indent the sublist
        slide[1].shift(RIGHT * 0.5)


        text = utils.get_text(f"text_to_speech/{lang}/program_execution_3.txt")
        with self.voiceover(text) as tracker:
            self.play(Write(slide))

        self.wait()
    