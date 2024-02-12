from manim import *
import setup
from manim_datastructures import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
from manim_voiceover.services.recorder import RecorderService
import os


class process_creation_fork(VoiceoverScene):
    def construct(self):
        # self.set_speech_service(
        #     AzureService(
        #         voice="nb-NO-FinnNeural",
        #         style="default",
        #     )
        # )
        self.set_speech_service(RecorderService())

        lang = os.getenv("LANG", "nor")
        example_code = VGroup(
            Text("main.c", color=WHITE),
            Code(
                file_name="code_examples/example2.c",
            )
        ).arrange(DOWN, aligned_edge=LEFT)\
            .scale(0.5)
        
        
        text = utils.get_text(f"text_to_speech/{lang}/process_creation_fork/1.txt")

        with self.voiceover(text=text) as tracker:
            self.play(Create(example_code), runtime=tracker.duration)


        self.play(example_code.animate.to_edge(UP), runtime=0.2)

        # the execution of the program
        example_execution = VGroup(
            Text("terminal"), 
            Code(file_name="code_examples/example2_output.txt", insert_line_no=False)
        ).arrange(DOWN, aligned_edge=LEFT)\
            .scale(0.5)\
            .next_to(example_code, DOWN, aligned_edge=LEFT)

        self.play(Create(example_execution), runtime=0.2)

        # animate to_edge left for both example_code and example_execution
        self.play(
            AnimationGroup(
                example_code.animate.to_edge(LEFT).shift(RIGHT),
                example_execution.animate.to_edge(LEFT).shift(RIGHT)
            ),
            runtime=0.2,
        )

        self.wait()

        # Create a bulleted list with the main points
        slide = VGroup(
            Text("fork()"),

            BulletedList(
            r"Lager en \textbf{duplikat} av den kallende prosessen. Lager kopi av det virtuelle adresse rommet, åpne fildeskriporer, etc.",
            r"Begge prosesser fortsetter å kjøre i parallell",
            r"Returnerer:",
            tex_environment="flushleft"
            ),

        # Create an indented sub-list for the return values
            BulletedList(
                r"hvis forelder: \textbf{barneprosessen sin PID} eller \textbf{-1} ved feil",
                r"hvis barn: \textbf{0} (ingen barneprosess blir opprettet dersom fork feiler)",
                tex_environment="flushleft"
            )
        ).arrange(DOWN, aligned_edge=LEFT)\
            .scale(0.4)\
            .next_to(example_code, RIGHT)\
            .shift((RIGHT/2) + (DOWN * 1.5))
        # indent the sub-list
        slide[2].shift(RIGHT * 0.5)

        # Shift the second list to the right to create an indentation effect

        # Add both lists to the scene, one after the other
        """
        fork() Lager en duplikat av den kallende prosessen. Den lager kopier av det virtuelle
        adresse rommet, åpne fildeskriptorer, og mye mer.

        Begge disse prosessene kommer til å fortsette i parallell.

        De returnerer:
            Foreldreprosessen returnerer barneprosessen sin PID ved suksess eller -1 ved feil
            
            Mens barneprosessen returnerer 0 ved suksess, hvis ikke feilet fork og det finnes ingen
            barneprosess
        """

        text = utils.get_text(f"text_to_speech/{lang}/process_creation_fork/2.txt")

        with self.voiceover(text=text) as tracker:
            self.play(Write(slide), runtime=0.5)

        # Keep the scene displayed for a while after everything has been written
        self.wait()


