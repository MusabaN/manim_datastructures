from manim import *


class process_creation_fork(Scene):
    def construct(self):
        example_code = VGroup(
            Text("main.c", color=WHITE),
            Code(
                file_name="code_examples/example2.c",
            )
        ).arrange(DOWN, aligned_edge=LEFT)\
            .scale(0.5)
        
        
        """
        Dette er et eksempel på bruk av fork()
        """

        self.play(Create(example_code))
        self.wait()

        self.play(example_code.animate.to_edge(UP))
        self.wait()

        # the execution of the program
        example_execution = VGroup(
            Text("terminal"), 
            Code(file_name="code_examples/example2_output.txt", insert_line_no=False)
        ).arrange(DOWN, aligned_edge=LEFT)\
            .scale(0.5)\
            .next_to(example_code, DOWN, aligned_edge=LEFT)

        self.play(Create(example_execution))
        self.wait()

        # animate to_edge left for both example_code and example_execution
        self.play(
            AnimationGroup(
                example_code.animate.to_edge(LEFT),
                example_execution.animate.to_edge(LEFT)
            )
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
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.3).to_edge(RIGHT)
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

        self.play(Write(slide))
        
        # Keep the scene displayed for a while after everything has been written
        self.wait()


