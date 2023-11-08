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

    def update_value(self, scene, value, index):
        self.table.add_highlighted_cell((index, 0), color=RED).animate()
        scene.wait(0.5)
        scene.remove(self.table)
        self.update_table()
        self.table.add_highlighted_cell((index, 0), color=RED).animate()
        scene.add(self.table)
        scene.wait(0.5)
        self.table.add_highlighted_cell((index, 0), color=BLACK).animate()
        scene.wait(0.5)
        scene.remove(self.table)
        self.update_table()
        scene.add(self.table)
        scene.wait(0.2)

    def update_pc(self, scene, val):
        self.num_table[0] = str(val)
        self.update_value(scene, val, 1)
    
    def update_bp(self, scene, val):
        self.num_table[1] = str(val)
        self.update_value(scene, val, 2)
    
    def update_sp(self, scene, val):
        self.num_table[2] = str(val)
        self.update_value(scene, val, 3)
    
    def update_acc(self, scene, val):
        self.num_table[3] = str(val)
        self.update_value(scene, val, 4)
        
    



class MyScene(Scene):
    def construct(self):
        cpu1 = m_cpu(0, 1, 2, 3)

        self.add(cpu1.group)

        self.wait(0.5)

        cpu1.update_pc(self, 20)

        cpu1.update_bp(self, 30)

        cpu1.update_sp(self, 40)

        cpu1.update_acc(self, 50)

        self.wait(0.5)