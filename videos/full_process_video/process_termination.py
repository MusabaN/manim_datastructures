from manim import *

#Notater for denne delen finnes i notes.md under Process termination
class process_termination(Scene):
    def construct(self):
        slide = VGroup(
            Text("En prosess kan avsluttes på flere forskjellige måter:"),
            BulletedList(
                "Ingen flere instruksjoner å utføre i programmet - ukjent statusverdi",
                "En funksjon i et program avslutter med en retur - parameter for å returnere statusverdien",
                r"Systemkallet \texttt{void exit(int status)} - avslutter en prosess og returnerer statusverdien (se man 3 exit)",
                r"Systemkallet \texttt{int kill(pid\_t pid, int sig)} - sender et signal for å avslutte en prosess (se man 2 kill, man 7 signal)",
            ),
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.7)
        
        self.add(slide)