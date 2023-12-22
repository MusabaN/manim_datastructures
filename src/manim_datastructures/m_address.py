from manim import *

class m_address(VGroup):
    """
    Docstring
    """

    def __init__(self,numberseq=[], scale = 1, title = "Virtual address", *args, **kwargs):
        """
        Params
        """
        super().__init__(*args,**kwargs)
        self.scale= scale


        self.table = Table([[str(x) for x in numberseq]], include_outer_lines=True).scale(self.scale)
        self.title = Text(title).scale(self.scale).next_to(self.table,UP)

        self.add(self.table,self.title)
            

    def highlight_cells(self,start_index,end_index,rgb=GREEN):
        for i in range(start_index+1,end_index+2):
            self.table.add_highlighted_cell((1,i),color=rgb)
        return self.table
    
    def highlight_cells_anim(self,start_index,end_index,rgb=GREEN,**kwargs):
        anims = []
        for i in range(start_index+1,end_index+2):
            cell_to_highlight = self.table.get_cell((1,i))
            anims.append(cell_to_highlight.animate.add_background_rectangle(rgb))
        anims.append(Wait())
        return LaggedStart(*anims,**kwargs)
    
    
    def group(self, start_index, end_index, rgb = YELLOW,**kwargs):
        #svg mobject av krøllparentes
        group_rectangle = SurroundingRectangle(self.table.get_entries(1,start_index,end_index),rgb)
        return LaggedStart(Create(group_rectangle),**kwargs)