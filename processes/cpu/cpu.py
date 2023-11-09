from manim import *

class m_cpu:
    """
    Params:
    pc - program counter
    bp - base pointer
    sp - stack pointer
    acc - accumulator

    Description:
    This class is used to create a cpu object, which is a group of
    rectangles and text objects. It is used to represent the cpu in
    the context of a process.
    """
    def __init__(self, pc, bp, sp, acc):
        self.pc = pc
        self.bp = bp
        self.sp = sp
        self.acc = acc
        self.pc_text = "PC"
        self.bp_text = "BP"
        self.sp_text = "SP"
        self.acc_text = "EAX"
        self.num_table = [
            str(self.pc), 
            str(self.bp), 
            str(self.sp), 
            str(self.acc),
            ]
        self.txt_table = [
            self.pc_text, 
            self.bp_text, 
            self.sp_text, 
            self.acc_text,
            ]
        

        self.update_table()

        self.table_title = Text("CPU")
        self.table_title.next_to(self.table, UP)
        self.group = Group(self.table, self.table_title)        
    
    """
    Description:
    This function returns the table object, which is a group of
    rectangles and text objects. It is used to represent the cpu in
    the context of a process.
    """
    def get_table(self):
        return self.table
    

    """
    Description:
    This function updates the table object, which is a group of
    rectangles and text objects. It is used to represent the cpu in
    the context of a process.
    """
    def update_table(self):
        self.con_table = [[s, str(n)] for s, n in zip(self.txt_table, self.num_table)]
        self.table = Table(self.con_table, include_outer_lines=True)
    

    """
    Description:
    This function updates a field of the cpu object, which is a group of
    rectangles and text objects. It is used to represent the cpu in
    the context of a process.
    """
    def update_value(self, scene, index, time):
        self.table.add_highlighted_cell((index, 0), color=GREEN)
        self.table[0].set_opacity(0)
        scene.play(self.table[0].animate.set_opacity(1), run_time=time/4)
        scene.wait(time/4)
        scene.remove(self.table)
        self.update_table()
        self.table.add_highlighted_cell((index, 0), color=GREEN)
        self.table[0].set_opacity(1)
        scene.add(self.table)
        scene.wait(time/4)
        scene.play(self.table[0].animate.set_opacity(0), run_time=time/4)




    def update_value2(self, scene, index, time):
        self.table.add_highlighted_cell((index, 0), color=RED)
        scene.wait(time/4)
        scene.remove(self.table)
        self.update_table()
        self.table.add_highlighted_cell((index, 0), color=RED)
        scene.add(self.table)
        scene.wait(time/4)
        self.table.add_highlighted_cell((index, 0), color=BLACK)
        scene.wait(time/4)
        scene.remove(self.table)
        self.update_table()
        scene.add(self.table)
        scene.wait(time/4)

    def update_pc(self, scene, val, time=3):
        self.num_table[0] = str(val)
        self.update_value(scene, 1, time)
    
    def update_bp(self, scene, val, time=3):
        self.num_table[1] = str(val)
        self.update_value(scene, 2, time=3)
    
    def update_sp(self, scene, val, time=3):
        self.num_table[2] = str(val)
        self.update_value(scene, 3, time=3)
    
    def update_acc(self, scene, val, time=3):
        self.num_table[3] = str(val)
        self.update_value(scene, 4, time)
        
    



class MyScene(Scene):
    def construct(self):
        cpu1 = m_cpu(0, 1, 2, 3)

        self.add(cpu1.group)

        cpu1.update_pc(self, 20)

        # cpu1.update_bp(self, 30, 3)

        # cpu1.update_sp(self, 40, 4)

        # cpu1.update_acc(self, 50, 5)
