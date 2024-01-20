from manim import *


class process_waiting(Scene):
    def construct(self):
        slide = VGroup(
            BulletedList(
                "For å få en prosess til å vente kan vi bruke systemkallet",
                r"pid_t wait(int *status)",
                "Gjør at kallende prosess venter til hvilken som helst av barneprossene termineres (hvis det finnes noen)",
                "Dette returnerer:",
                tex_environment="flushleft"
            ),
            BulletedList(
                r"\textbf{-1} Hvis ingen barneprosesser eksisterer",
                r"\textbf{PID} til den terminerte barneprosessen og legger statusen til prosessen i \textbf{status}",
                tex_environment="flushleft"
            )
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.7)

        """
        For å få en prosess til å vente kan vi bruke systemkallet wait
        Wait gjør at kallende prosess vil vente til hvilken som helst av barneprosessene terminerer, om de eksisterer

        Wait returnerer
        prosess id til den terminerte barneprosessen og lagrer statusen til prosessen i statusvariabelen
        -1 hvis ingen barneprosesser finnes       
        """
        
        self.add(slide)