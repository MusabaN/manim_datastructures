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
        self.set_speech_service(RecorderService())

        lang = os.environ.get("LANG", "eng")

        cr3_text = Text("CR3")
        cr3_box = Square().surround(cr3_text, buff=0.5)
        cr3 = VGroup(cr3_text, cr3_box).shift(UL * 2).scale(0.7)
        top_directory = m_memory(num_cells=8).to_edge(DOWN)
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

        text = utils.get_text(f"text_to_speech/{lang}/virtual_memory/2.txt")
        math_equation = MathTex(
            '2^{10} = 1024',
        )
        with self.voiceover(text=text) as tracker:
            self.play(Create(arr))
            self.wait()

            self.wait_until_bookmark('A')
            self.play(Create(math_equation))

        self.play(Uncreate(math_equation))
        self.wait()

        text = utils.get_text(f"text_to_speech/{lang}/virtual_memory/3.txt")
        with self.voiceover(text=text) as tracker:
            self.wait_until_bookmark('POPUP_FIRST')
            self.play(arr.animate.multi_popup(0, 3))
            self.wait_until_bookmark('POPDOWN_FIRST')
            self.play(arr.animate.multi_popdown(0, 3))
            self.wait_until_bookmark('POPUP_SECOND')
            self.play(arr.animate.multi_popup(3, 6))
            self.wait_until_bookmark('POPDOWN_SECOND')
            self.play(arr.animate.multi_popdown(3, 6))
            self.wait_until_bookmark('POPUP_LAST')
            self.play(arr.animate.multi_popup(6, 10))
            self.wait_until_bookmark('POPDOWN_LAST')
            self.play(arr.animate.multi_popdown(6, 10))

        binary_conversion = MathTex(
            '101 = 5'
        )
        offset_line_1 = None
        brace1 = None
        text = utils.get_text(f"text_to_speech/{lang}/virtual_memory/4.txt")
        with self.voiceover(text=text) as tracker:
            self.wait_until_bookmark('POPUP_FIRST')
            self.play(arr.animate.multi_popup(0, 3))
            self.wait_until_bookmark('SHOW_BINARY_CONVERSION')
            self.play(Create(binary_conversion))
            self.wait_until_bookmark('HIDE_BINARY_CONVERSION')
            self.play(Uncreate(binary_conversion))
            self.wait_until_bookmark('DRAW_ARROW')
            brace1 = BraceBetweenPoints(
                arr.get_coord(0, LEFT),
                arr.get_coord(2, RIGHT),
                UP,
            )
            offset_line_1 = m_orthogonal_line(
                brace1.get_tip(),
                path=[
                    (top_directory.get_critical_point(DL) + DL / 2, "|-"),
                    (top_directory.get_cell_position_center(5, LEFT), "|-"),
                ],
                color=BLUE,
            )
            offset_line_1.add(offset_line_1.create_tip())
            self.play(Create(brace1))
            self.play(Create(offset_line_1))

        self.wait()
        second_level_directory = m_memory(num_cells=8) \
            .scale(0.65) \
            .align_to(top_directory, RIGHT) \
            .shift(RIGHT * 5 + UP * 0.6)

        arrow_to_second_level_directory = m_orthogonal_line(
            top_directory.get_cell_position_center(5, RIGHT),
            path=[
                (second_level_directory.get_critical_point(UL) + UL / 2, "-|--"),
                (second_level_directory.get_edge_center(UP), "-|"),
            ],
        )
        arrow_to_second_level_directory.add(arrow_to_second_level_directory.create_tip())
        top_dir_address = MathTex(
            '1010011',
        )
        top_dir_addres_present = MathTex(
            '0',
            color=RED,
        )

        top_dir_address_group = VGroup(
            top_dir_address,
            top_dir_addres_present,
        ).arrange(RIGHT, buff=0.05) \
            .scale(0.5) \
            .move_to(top_directory.get_cell_position_center(5, RIGHT)) \
            .shift(LEFT * (top_directory.width / 2))

        text = utils.get_text(f"text_to_speech/{lang}/virtual_memory/5.txt")
        with self.voiceover(text=text) as tracker:
            self.play(Create(top_dir_address_group))
            self.wait_until_bookmark('TURN_GREEN')
            self.play(top_dir_addres_present.animate.become(
                MathTex(
                    '1',
                    color=GREEN,
                ).scale(0.5)\
                    .move_to(top_dir_addres_present.get_center())
            ))

        text = utils.get_text(f"text_to_speech/{lang}/virtual_memory/6.txt")
        with self.voiceover(text=text) as tracker:
            self.play(Create(second_level_directory))
            self.play(Create(arrow_to_second_level_directory))

        self.wait()
        text = utils.get_text(f"text_to_speech/{lang}/virtual_memory/7.txt")
        brace2 = None
        offset_line_2 = None
        with self.voiceover(text=text) as tracker:
            self.wait_until_bookmark('POPUP_SECOND')
            self.play(arr.animate.multi_popup(3, 6))
            self.wait_until_bookmark('BRACE_AND_ARROW')
            brace2 = BraceBetweenPoints(
                arr.get_coord(3, LEFT),
                arr.get_coord(5, RIGHT),
                UP,
            )
            self.play(Create(brace2))
            self.wait()
            offset_line_2 = m_orthogonal_line(
                brace2.get_tip(),
                path=[
                    (second_level_directory.get_critical_point(DL) + DL / 2, "|-"),
                    (second_level_directory.get_cell_position_center(3, LEFT), "|-"),
                ],
                color=BLUE,
            )
            offset_line_2.add(offset_line_2.create_tip())
            self.play(Create(offset_line_2))

        self.wait()

        # make another address and present bit and group it
        second_dir_address = MathTex(
            '0100101',
        )
        second_dir_addres_present = MathTex(
            '0',
            color=RED,
        )

        second_dir_address_group = VGroup(
            second_dir_address,
            second_dir_addres_present,
        ).arrange(RIGHT, buff=0.05) \
            .scale(0.5) \
            .move_to(second_level_directory.get_cell_position_center(3, RIGHT)) \
            .shift(LEFT * (second_level_directory.width / 2))


        text = utils.get_text(f"text_to_speech/{lang}/virtual_memory/8.txt")
        with self.voiceover(text=text) as tracker:
            self.play(Create(second_dir_address_group))
            self.wait_until_bookmark('TURN_GREEN')
            self.play(second_dir_addres_present.animate.become(
                MathTex(
                    '1',
                    color=GREEN,
                ).scale(0.5)\
                    .move_to(second_dir_addres_present.get_center())
            ))

        self.wait()

        page = m_page(
            width=second_level_directory.width + 1,
            height=second_level_directory.height,
            num_cells=16,
        ).align_to(second_level_directory, RIGHT) \
            .shift((RIGHT * 5) + (UP * 0.6))

        arrow_to_page = m_orthogonal_line(
            second_level_directory.get_cell_position_center(3, RIGHT),
            path=[
                (page.get_critical_point(UL) + UL / 2, "-|--"),
                (page.get_edge_center(UP), "-|"),
            ],
        )
        arrow_to_page.add(arrow_to_page.create_tip())

        text = utils.get_text(f"text_to_speech/{lang}/virtual_memory/9.txt")
        brace3 = None
        offset_line_3 = None
        with self.voiceover(text=text) as tracker:
            self.wait_until_bookmark('FADEIN_PAGE')
            self.play(Create(page))
            self.wait_until_bookmark('DRAW_ARROW')
            self.play(Create(arrow_to_page))
            self.wait_until_bookmark('POPUP_LAST')
            self.play(arr.animate.multi_popup(6, 10))
            self.wait_until_bookmark('BRACE_AND_ARROW')
            brace3 = BraceBetweenPoints(
                arr.get_coord(6, LEFT),
                arr.get_coord(9, RIGHT),
                UP,
            )
            self.play(Create(brace3))
            self.wait()
            offset_line_3 = m_orthogonal_line(
                brace3.get_tip(),
                path=[
                    (page.get_critical_point(DL) + DL / 2, "|-"),
                    (page.get_cell_position_center(0, LEFT), "|-"),
                ],
                color=BLUE,
            )
            offset_line_3.add(offset_line_3.create_tip())
            self.play(Create(offset_line_3))

        self.wait()

        text = utils.get_text(f"text_to_speech/{lang}/virtual_memory/10.txt")



        self.add(top_dir_address_group)

        self.wait(10)



