from manim import *

class m_angled_arrow(VGroup):
    def __init__(self,start,end,dir):
        super().__init__()
        self.start = start
        self.end = end
        self.dir = dir
        self.line_coord = np.array([0,0,0])

        self.start_buff()
        
        line = self.draw_line()
        arrow_to_end = Arrow(self.line_coord,self.end,buff=0)
        self.add(line,arrow_to_end)


    def draw_line(self):
        if self.dir == "x":
            self.line_coord = np.array([self.end[0],self.start[1],0])
            return Line(start=self.start,end=self.line_coord)
        if self.dir == "y":
            self.line_coord = np.array([self.start[0],self.end[1],0])
            return Line(start=self.start,end=self.line_coord)
            
    def start_buff(self):
        start_x = self.start[0]
        start_y = self.start[1]
        end_x = self.end[0]
        end_y = self.end[1]

        height_diff = start_y-end_y
        width_diff = start_x-end_x 

        if self.dir == "y":
            if height_diff>0:
                self.start[1] = self.start[1]-0.1
            elif height_diff<0:
                self.start[1] = self.start[1]+0.1
        elif self.dir == "x":
            if width_diff>0:
                self.start[0] = self.start[0]-0.1
            elif width_diff<0:
                self.start[0] = self.start[0]+0.1

    
