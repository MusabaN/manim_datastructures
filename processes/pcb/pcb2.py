from manim import *

class PCBAnimation(Scene):
    def construct(self):
        # Define properties of the text elements
        font_size = 24
        color = "black"
        # Define the text elements
        header = Text("PCB", font_size=font_size+6, color=color)
        pid_label = Text("PID:", font_size=font_size, color=color)
        pid_value = Text("0x00", font_size=font_size, color=color)
        pc_label = Text("PC:", font_size=font_size, color=color)
        pc_value = Text("0x00", font_size=font_size, color=color)
        bp_label = Text("BP:", font_size=font_size, color=color)
        bp_value = Text("0x00", font_size=font_size, color=color)
        sp_label = Text("SP:", font_size=font_size, color=color)
        sp_value = Text("0x00", font_size=font_size, color=color)
        eax_label = Text("EAX:", font_size=font_size, color=color)
        eax_value = Text("0x00", font_size=font_size, color=color)
        # Define the padding for the rectangle and the vertical spacing between elements
        padding = 0.5
        spacing = 0.5
        # Calculate the maximum width and height of the text elements
        max_width = max(
            header.get_width(),
            pid_label.get_width(),
            pid_value.get_width(),
            pc_label.get_width(),
            pc_value.get_width(),
            bp_label.get_width(),
            bp_value.get_width(),
            sp_label.get_width(),
            sp_value.get_width(),
            eax_label.get_width(),
            eax_value.get_width(),
        )
        max_height = max(
            header.get_height(),
            pid_label.get_height(),
            pid_value.get_height(),
            pc_label.get_height(),
            pc_value.get_height(),
            bp_label.get_height(),
            bp_value.get_height(),
            sp_label.get_height(),
            sp_value.get_height(),
            eax_label.get_height(),
            eax_value.get_height(),
        )

        # Create the rectangle based on the maximum width and height of the text elements
        header_padding = 2
        pcb_table = RoundedRectangle(
            width=max_width * 3 + padding * 5,
            height=(max_height + spacing) * 5 + padding *
            2 + header.get_height() + header_padding,
            stroke_color=WHITE,
            stroke_width=1,
            fill_opacity=1,
            fill_color=WHITE,
        )

        
        line = Line(color = BLACK)
        line.width = pcb_table.get_width()


# Position the text elements relative to the rectangle's center
        current_x = pcb_table.get_left()[0] + padding + max_width / 2
        current_y = pcb_table.get_top()[1] - padding - max_height / 2
        # Position and add each text element to the rectangle
        pid_label.move_to([current_x - max_width / 2,
                          current_y - (max_height + spacing), 0])
        pid_value.move_to([current_x + max_width / 2 + padding,
                          current_y - (max_height + spacing), 0])
        pc_label.move_to([current_x - max_width / 2,
                         current_y - 2*(max_height + spacing), 0])
        pc_value.move_to([current_x + max_width / 2 + padding,
                         current_y - 2*(max_height + spacing), 0])
        bp_label.move_to([current_x - max_width / 2,
                         current_y - 3 * (max_height + spacing), 0])
        bp_value.move_to([current_x + max_width / 2 + padding,
                         current_y - 3 * (max_height + spacing), 0])
        sp_label.move_to([current_x - max_width / 2,
                         current_y - 4 * (max_height + spacing), 0])
        sp_value.move_to([current_x + max_width / 2 + padding,
                         current_y - 4 * (max_height + spacing), 0])
        eax_label.move_to([current_x - max_width / 2,
                          current_y - 5 * (max_height + spacing), 0])
        eax_value.move_to([current_x + max_width / 2 + padding,
                          current_y - 5 * (max_height + spacing), 0])
        header.move_to([0, current_y,0])
        line.next_to(header,DOWN)

        # Add the text elements to the rectangle
        pcb_table.add(
            header,
            line,
            pid_label,
            pid_value,
            pc_label,
            pc_value,
            bp_label,
            bp_value,
            sp_label,
            sp_value,
            eax_label,
            eax_value,
        )
        # Add the header and line to the rectangle
        
        # Re-position the rectangle to span over the text elements
        pcb_table.move_to(ORIGIN)
        pcb_table.stretch_to_fit_width(max_width * 3 + padding * 5)
        self.play(FadeIn(pcb_table))
