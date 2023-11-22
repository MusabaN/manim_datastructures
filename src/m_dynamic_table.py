from manim import *
import ctypes

VAL = ctypes.c_int(0).value
IND = ctypes.c_int(1).value
HEX = ctypes.c_int(2).value

class m_dynamic_table:
    # tyype infer left_col and right_col to be lists
    def __init__(self, title, left_col: list, right_col: list):
        if (len(left_col) != len(right_col)):
            raise Exception("left_col and right_col must have the same length")
        self.dict = {}
        i = 1
        for key, val in zip(left_col, right_col):
            self.dict[key] = (val, i, self.hexit(val))
            i += 1
        
        self.update_table()
        self.title = Text(title)
        self.title.next_to(self.table, UP)
        self.group = VGroup(self.table, self.title)
    
    def hexit(self, val):
        return val
        pass
        # Make it so that you return val, but as a string 0x00000

    def update_table(self):
        self.table = Table([[s, str(right[VAL])] for s, right in self.dict.items()], include_outer_lines=True)

    def update_value(self, scene, key, val, time, color=GREEN):
        # Highlight cell
        self.table.add_highlighted_cell((self.dict[key][IND], 0), color=color)
        self.table[0].set_opacity(0)
        scene.play(self.table[0].animate.set_opacity(1), run_time=time/4)
        scene.wait(time/4)

        # Update cell content
        self.dict[key] = (val, self.dict[key][IND])
        scene.remove(self.table)
        self.update_table()
        self.table.add_highlighted_cell((self.dict[key][IND], 0), color=color)
        self.table[0].set_opacity(1)
        scene.add(self.table)
        scene.wait(time/4)

        # Remove highlight
        scene.play(self.table[0].animate.set_opacity(0), run_time=time/4)
        scene.remove(self.table)
        self.update_table()
        scene.add(self.table)


    def get_dict(self):
        return self.dict
    

# if name main
if __name__ == "__main__":
    test = m_dynamic_table(["PC", "BP", "SP", "EAX"], [10,20,30,40])
    print(test.get_dict())

class TestDynamicTable(Scene):
    def construct(self):
        cpu = m_dynamic_table("CPU", ["PC", "BP", "SP", "EAX"], [10,20,30,40])
        self.add(cpu.group)

        cpu.update_value(self, "PC", 100, 2)

        cpu.update_value(self, "BP", 200, 2)