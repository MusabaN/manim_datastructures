from manim import *

class Cpu(VGroup):
    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data
        self.table_title = Text("CPU")
        self.update_table()
    
    def set(self, register, value):
        self.data[register] = value
        self.update_table()
    
    def unset(self, register):
        del self.data[register]
        self.update_table()

    def update_table(self):
        self.con_table = [[s, f"0x{n:03x}"] for s, n in self.data.items()]
        self.table = Table(self.con_table, include_outer_lines=True)
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
    
    def push(self, value):
        return Cpu(self.data + value)
    
    def pop(self, register, **kwargs):
        anims = []
        anims.append(self.animate.unset(register))
        anims.append(Wait())
        return Succession(*anims, **kwargs)

    def update_pc(self, scene, val, time=3):
        self.num_table[0] = f"{val:02x}"    
        self.update_value(scene, 1, time)

class MyScene(Scene):
    def construct(self):
        cpu1 = Cpu(data= {
            "PC": 0,
            "BP": 1,
            "SP": 2,
            "EAX": 3,
        })
        self.add(cpu1)
        self.play(cpu1.animate_change("PC", 0x20, run_time=2, rate_func=linear))
        self.wait()
        self.play(cpu1.animate_change("EAX", 0x05, run_time=2, rate_func=linear))
        self.wait()
        update_cpu = cpu1.push(100)
        self.play(FadeTransform(cpu1, update_cpu))
        self.wait(5)
