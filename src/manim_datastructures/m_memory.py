from manim import *
import numpy as np

class m_memory(VGroup):
    
    def __init__(self, height=5, width=2, num_cells = 4):
        super().__init__()

        self.rect = Rectangle(height=height, width=width)
        self.num_cells = num_cells

        start = self.rect.get_corner(UL)
        end = self.rect.get_corner(DL)

        between = (end - start) / num_cells
        
        start += between

        for _ in range(num_cells):
            self.add(Line(start, (start + (RIGHT * width))))
            start += between
        
        self.between = between

        self.add(self.rect)
    

    def get_cell_position(self, cell_num, pos):
        if np.array_equal(pos, LEFT):
            return (self.rect.get_corner(UL) + (self.between * cell_num))
        else:
            return (self.rect.get_corner(UR) + (self.between * cell_num))
    
    def color_between(self, other_memory: 'm_memory', color: 'manim_colors', start_1, start_2, distance, direction=RIGHT):
        dir1, dir2 = LEFT, RIGHT
        if np.array_equal(direction, RIGHT):
            dir1, dir2 = RIGHT, LEFT
        
        polys = VGroup()
        for i, j in zip(range(start_1, start_1 + distance), range(start_2, start_2 + distance)):
            s1 = self.get_cell_position(i, dir1)
            e1 = self.get_cell_position(i+1, dir1)
            s2 = other_memory.get_cell_position(j, dir2)
            e2 = other_memory.get_cell_position(j+1, dir2)

            color_bounds = color

            if i < 0 or i >= self.num_cells:
                color_bounds = RED
            if j < 0 or j >= other_memory.num_cells:
                color_bounds = RED
            
            polys.add(Polygon(s1, e1, e2, s2,
                              color=color_bounds, 
                    fill_opacity=0.2,
                    stroke_width=0))
            
        return polys