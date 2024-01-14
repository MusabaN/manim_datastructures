from manim import *
import setup
from manim_datastructures import *


class process_creation(Scene):

    def construct(self):
        example_code = VGroup(
            Text("main.py"),
            Code(
                file_name="code_examples/example1.py",
            )
        ).arrange(DOWN, aligned_edge=LEFT)
        

        self.play(Create(example_code))
        self.wait()

        # this is a program

        # a process is a result of the execution of the program


        self.play(example_code.animate.to_edge(UP))
        example_execution = VGroup(
            Text("terminal"), 
            Code(file_name="code_examples/example1_output.txt", insert_line_no=False)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(example_code, DOWN, aligned_edge=LEFT)
        self.play(Create(example_execution))
        self.wait()




