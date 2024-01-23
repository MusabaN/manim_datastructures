from manim import *
import setup
from manim_datastructures import *
from manim.mobject.text.text_mobject import remove_invisible_chars


class program_execution(Scene):

    def construct(self):

        macode = utils.create_code(
                "code_examples/example3.c",
            )

        example_code = VGroup(
            Text("main.c"),
            remove_invisible_chars(macode)
        ).arrange(DOWN, aligned_edge=LEFT)\
            .scale(0.5)
        
        
        self.add(example_code)

        """
        Nå skal vi se på programeksekvering
        """

        # highlight line number 15
        highlight = BackgroundRectangle(macode.code[14], color=GREEN, fill_opacity=0.2)\
                        .stretch_to_fit_width(macode.width).align_to(macode, LEFT)


        """
        Vi kan se på linje 15 et eksempel på eksekvering av et program ved systemkallet execve
        """
        self.play(Create(highlight))
        self.wait()

        self.play(Uncreate(highlight))
        self.wait()

        slide = VGroup(
            BulletedList(
                "For å eksekvere et program kan man bruke blant annet",
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
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.3).to_edge(RIGHT)

        # Indent the sublist
        slide[1].shift(RIGHT * 0.5)

        self.play(example_code.animate.to_edge(LEFT))
        self.wait()

        """
        Systemkallet execve kjører programmet som er pekt på av filename, og sender med argumentene
        i argv og i miljøet gitt av envp

        Dette returnerer ingenting ved suksess, for da bytter vi til den nye prosessen
        ved feil returneres -1         
        """

        self.play(Write(slide))
        self.wait()
    