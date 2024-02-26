from manim import *
import setup
from manim_datastructures import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService
from manim_voiceover.services.recorder import RecorderService
from manim_voiceover.services.gtts import GTTSService
import os


class VirtualMemory(VoiceoverScene, MovingCameraScene):
    def construct(self):
        # self.set_speech_service(
        #     AzureService(
        #         voice="en-US-DavisNeural",
        #         style="friendly",
        #     )
        # )
        self.set_speech_service(GTTSService(lang="en", tld="com", transcription_model='base'))

        lang = os.environ.get("LANG", "nor")

        cr3_text = Text("CR3")
        cr3_box = Square().surround(cr3_text, buff=0.5)
        cr3 = VGroup(cr3_text, cr3_box).shift(UL * 2).scale(0.7)
        top_directory = m_memory(num_cells=10).to_edge(DOWN)
        arrow_from_cr3_to_top_directory = m_orthogonal_line(
            cr3.get_edge_center(RIGHT),
            top_directory.get_edge_center(UP),
            "-|",
        )
        arrow_from_cr3_to_top_directory.add(arrow_from_cr3_to_top_directory.create_tip())

        text = utils.get_text(f"text_to_speech/{lang}/virtual_memory/1.txt")
        with self.voiceover(text=text) as tracker:
            self.play(Create(cr3))
            self.wait_until_bookmark('A')

            self.play(Create(top_directory))
            self.play(Create(arrow_from_cr3_to_top_directory))
            self.wait()

            # move camera so that cr3 is in the top left
            # self.camera.frame.save_state()
            # self.play(self.camera.frame.animate.set(height=12).to_edge(UL))

            self.play(
                VGroup(
                    cr3, top_directory, arrow_from_cr3_to_top_directory
                ).animate \
                    .to_edge(UL).scale(0.65) \
                    .shift(UP * 0.5 + LEFT * 0.5),
            )

            self.wait()

        arr = m_virtual_address(
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 0]
        ).to_edge(DL).shift(RIGHT * 1.85).scale(0.8)

        self.play(Create(arr))
        self.wait()
        self.play(arr.animate.multi_popup(0, 3))
        self.wait()
        brace1 = BraceBetweenPoints(
            arr.get_coord(0, LEFT),
            arr.get_coord(2, RIGHT),
            UP,
        ).shift(UP * 0.25)

        self.play(Create(brace1))
        self.wait()

        # create a lambda function
        # that creates a line from the tip of the brace
        # to the top directory

        offset_line_1 = m_orthogonal_line(
            brace1.get_tip(),
            path=[(brace1.get_tip() + .5 * UP, "|"),
                  (top_directory.get_critical_point(DL) + DL, "-"),
                  (top_directory.get_cell_position(4, LEFT), "|-"),
                  ],
            color=BLUE,
        )
        offset_line_1.add(offset_line_1.create_tip())

        test_dot = Dot(color=RED).move_to(top_directory.get_cell_position(4, LEFT))

        self.play(Create(offset_line_1))
        self.play(Create(test_dot))
        self.wait(4)
