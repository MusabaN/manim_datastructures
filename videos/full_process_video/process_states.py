from manim import *
import setup
from manim_datastructures import *


class process_states(Scene):
    def construct(self):
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
        Vi nevnte noe tidligere om tilstander, det skal vi se på nå
        """


        """
        Først ser vi en full ready queue, det betyr at alle prosessene her er i tilstanden ready
        Det betyr at de er klare til å kjøre så fort de har tilgang
        """
        self.play(AnimationGroup(
            ready_queue.dequeue(),
            running_process_text.animate.become(Text("1").move_to(rect2.get_center())),
        ))

        """
        Her har prosess 1 fått tilgang til å kjøre, som nå har tilstanden running og utfører 
        instruksjonene den har
        """

        self.wait()

        self.play(AnimationGroup(
            block_queue.enqueue(1),
            running_process_text.animate.become(Text("").move_to(rect2.get_center())),
        ))

        """
        Nå ser vi at prosess 1 har havnet i blocked queue, da den har fått tilstanden blocked.
        Dette betyr at den har fått tilstanden blocked, noe som kan ha skjedd hvis den for eksempel
        venter på en input. Da venter vi på en ekstern hendelse før prosessen kan fortsette.
        """


        self.wait()

        self.play(AnimationGroup(
            ready_queue.dequeue(),
            running_process_text.animate.become(Text("2").move_to(rect2.get_center())),
        ))

        self.wait()

        """
        Prosess 2, som ble kjørende etter 1 ble blokkert, fullfører nå sine instruksjoner og termineres
        """

        kill_text = Text("Process end").to_edge(UR)

        self.play(
            Succession(
                Write(kill_text),
                running_process_text.animate.next_to(kill_text, DOWN, buff=0.3),
            )
        )
        self.wait()

        self.play(
            AnimationGroup(
                running_process_text.animate.become(Text("").next_to(kill_text, DOWN, buff=0.3)),
                Unwrite(kill_text),
            )
        )
        self.wait()

        running_process_text.move_to(rect2.get_center())
        running_process_text.text = ""
        
        """
        Nå blir prosess 3 kjørende, men vi ser at det eksterne som prosess 1 ventet på har kommet,
        da velger vi å fortsette prosess 1, mens scheduler flytter prosess 3 tilbake til ready queuen 
        """
        
        self.play(
            AnimationGroup(
                    ready_queue.dequeue(),
                    running_process_text.animate.become(Text("3").move_to(rect2.get_center())),
                )
        )

        self.wait()

        # put running process back on ready_queue and add blocked queue to running process
        self.play(
            AnimationGroup(
                ready_queue.enqueue(3),
                block_queue.dequeue(),
                running_process_text.animate.become(Text("1").move_to(rect2.get_center())),
            )
        )
        self.wait()
