from manim import *

class m_table(VGroup):
    def __init__(self, data, title="Table",scale=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scale = scale
        self.data = data
        self.table_title = Text(str(title)).scale(self.scale)
        self.update_table()
    
    def set(self, register, value):
        self.data[register] = value
        self.update_table()
    
    def unset(self, register):
        del self.data[register]
        self.update_table()

    def update_table(self):
        self.con_table = [[s, f"0x{n:03x}"] for s, n in self.data.items()]
        self.table = Table(self.con_table, include_outer_lines=True).scale(self.scale)
        self.table_title.next_to(self.table, UP)
        self.become(VGroup(self.table, self.table_title))
    
    def animate_change(self, register, value, **kwargs):
        anims = []
        index = list(self.data.keys()).index(register)+1
        self.table.add_highlighted_cell((index, 0), color=GREEN)
        self.table[0].set_z_index(-1).set_opacity(0)
        anims.append(self.table[0].animate.set_opacity(1).build())
        anims.append(Wait())
        anims.append(self.animate.set(register, value))
        anims.append(Wait())
        anims.append(self.table[0].animate.set_opacity(0).build())
        return Succession(*anims, **kwargs)
    
    def highlight_cell(self, register, **kwargs):
        anims = []
        index = list(self.data.keys()).index(register)+1
        self.table.add_highlighted_cell((index, 0), color=GREEN)
        self.table[0].set_z_index(-1).set_opacity(0)
        anims.append(self.table[0].animate.set_opacity(1).build())
        anims.append(Wait())
        anims.append(self.animate.set(register, self.data[register]))
        anims.append(Wait())
        anims.append(self.table[0].animate.set_opacity(0).build())
        return Succession(*anims, **kwargs)



if __name__ == "__main__":
    class theScene(Scene):
        def construct(self):
            cpu1 = m_table(data= {
                "PC": 0,
                "BP": 1,
                "SP": 2,
                "EAX": 3,
            }).scale(0.75)
            self.add(cpu1)
            self.play(cpu1.animate_change("PC", 0x20, run_time=2, rate_func=linear))
            self.wait()
            self.play(cpu1.animate_change("EAX", 0x05, run_time=2, rate_func=linear))
            self.wait()
            self.play(cpu1.highlight_cell("EAX", run_time=2, rate_func=linear))
            self.wait()
        
    import os
    os.system("manim -p -ql ./m_table.py theScene")
    input("Press Enter to continue...")
    os.system("rm -rf ./__pycache__")
    os.system("rm -rf ./media")

    