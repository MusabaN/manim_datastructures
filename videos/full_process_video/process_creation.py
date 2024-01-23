from manim import *
import setup
from manim_datastructures import *

#Notater for denne delen finnes i notes.md under Process creation

class process_creation(Scene):

    def construct(self):
        example_code = VGroup(
            Text("main.py"),
            Code(
                file_name="code_examples/example1.py",
            )
        ).arrange(DOWN, aligned_edge=LEFT)
        
        """
        Dette er et eksempel på et program
        """
        
        self.play(Create(example_code))
        self.wait()

        """
        Eksekveringen av et program kaller vi prosess
        Ved kjøringen av et program får vi en del tilstandsinformasjon
        Som for eksempel prosess id, pekere til minneområder, tilstand, signaler,
        pekere til stacken, osv
        Denne informasjonen må lagres, som også er en del av prosessen.

        En prosess kan lage en annen prosess ved hjelp av for eksempel fork(),
        som vi skal se videre på nå
        """

        self.play(example_code.animate.to_edge(UP))
        example_execution = VGroup(
            Text("terminal"), 
            Code(file_name="code_examples/example1_output.txt", insert_line_no=False)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(example_code, DOWN, aligned_edge=LEFT)
        self.play(Create(example_execution))
        self.wait()




