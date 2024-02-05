from manim import *
import setup
from manim_datastructures import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
import os


class process_states(VoiceoverScene):
    def construct(self):
        self.set_speech_service(
            AzureService(
                voice="nb-NO-FinnNeural",
                style="default",
            )
        )
        lang = os.environ.get("LANG", "nor")

        block_queue = m_queue(title="Blocked Queue", scale=0.7).to_edge(DL)
        ready_queue = m_queue(title="Ready Queue", scale=0.7)\
            .next_to(block_queue, UP, aligned_edge=RIGHT)

        for i in range(1, 5):
            ready_queue.enqueue_inner(i)

        self.add(block_queue, ready_queue)


        running_process = Text("Running Process").to_edge(UP)
        rect = SurroundingRectangle(running_process, buff=0.3, color=WHITE)
        rect2 = Rectangle(width=rect.width, height=3).next_to(rect, DOWN, buff=0)

        running_process_text = Text("").move_to(rect2.get_center())

        self.add(running_process, rect, rect2, running_process_text)

        """
        Nå skal vi se på tilstander en prosess kan være i. 
        Først ser vi en full ready queue, det betyr at alle prosessene her er i tilstanden ready
        Det betyr at de er klare til å kjøre så fort de har tilgang
        """
        text = utils.get_text(f"text_to_speech/{lang}/process_states_1.txt")
        with self.voiceover(text=text) as tracker:
            self.wait(tracker.duration)

        self.play(AnimationGroup(
            ready_queue.dequeue(),
            running_process_text.animate.become(Text("1").move_to(rect2.get_center())),
        ))

        """
        Her har prosess 1 fått tilgang til å kjøre, som nå har tilstanden running og utfører 
        instruksjonene den har
        """

        text = utils.get_text(f"text_to_speech/{lang}/process_states_2.txt")
        with self.voiceover(text=text) as tracker:
            self.wait(tracker.duration)


        self.play(AnimationGroup(
            block_queue.enqueue(1),
            running_process_text.animate.become(Text("").move_to(rect2.get_center())),
        ))

        """
        Nå ser vi at prosess 1 har havnet i blocked queue, da den har fått tilstanden blocked.
        Dette betyr at den har fått tilstanden blocked, noe som kan ha skjedd hvis den for eksempel
        venter på en input. Da venter vi på en ekstern hendelse før prosessen kan fortsette.
        """

        text = utils.get_text(f"text_to_speech/{lang}/process_states_3.txt")
        with self.voiceover(text=text) as tracker:
            self.wait(tracker.duration)

        self.play(AnimationGroup(
            ready_queue.dequeue(),
            running_process_text.animate.become(Text("2").move_to(rect2.get_center())),
        ))

        self.wait()

        """
        """

        kill_text = Text("Process end").to_edge(UR)

        text = utils.get_text(f"text_to_speech/{lang}/process_states_4.txt")
        with self.voiceover(text=text) as tracker:
            self.play(
                Write(kill_text),
                run_time=tracker.duration/3
            )
            self.play(

                running_process_text.animate.next_to(kill_text, DOWN, buff=0.3),
                run_time=tracker.duration/3
            )
            self.play(
                AnimationGroup(
                    FadeOut(
                        running_process_text
                    ),
                    Unwrite(kill_text),
                ),
                run_time=tracker.duration/3
            )
            self.play(
                running_process_text.animate.become(
                    Text("").move_to(running_process_text.get_center())),
                run_time=0
            )

        self.wait()

        running_process_text.move_to(rect2.get_center())
        running_process_text.text = ""
        
        """
        Nå blir prosess 3 kjørende. Vi ser at det eksterne som prosess 1 
        ventet på nå har blitt ferdig. da settes 1 først i ready queue.
        Prosess 3 bruker opp sitt tidsvindu og blir lagt bakerst i ready
        queue og prosess 1 byttes inn.
        """

        text = utils.get_text(f"text_to_speech/{lang}/process_states_5.txt")
        with self.voiceover(text=text) as tracker:
            self.play(
                    AnimationGroup(
                        ready_queue.dequeue(),
                        running_process_text.animate.become(Text("3").move_to(rect2.get_center())),
                    ),
                run_time=tracker.duration/5
            )
            self.play(
                Succession(
                    block_queue.dequeue(),
                    ready_queue.enqueue_front(1),
                ),
                run_time=tracker.duration/5
            )
            self.play(
                Succession(
                    ready_queue.enqueue(3),
                    ready_queue.dequeue(),
                    running_process_text.animate.become(Text("1").move_to(rect2.get_center())),
                ),
                run_time=tracker.duration/5
            )

        self.wait()