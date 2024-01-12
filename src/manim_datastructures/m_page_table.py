from manim import *

class m_page_table(VGroup):
    def __init__(self,num_of_entries=6,title="",scale = 1,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.scale = scale
        self.items = []
        self.page = self.create_page(num_of_entries) 
        self.title = Text(title).scale(self.scale).next_to(self.page, UP)
        self.add(self.title,self.page)



    def create_page(self, num_of_entries):
        group = VGroup()
        if num_of_entries >= 1:
            first_box = self.create_text_box()
            group.add(first_box)
            self.items.append(first_box)
            prev = first_box
            for i in range (1,num_of_entries):
                new_elem = self.create_text_box().next_to(prev,DOWN,buff=0)
                self.items.append(new_elem)
                group.add(new_elem)
                prev = new_elem
        
        return group

    def create_text_box(self):
        result = VGroup()
        box = Rectangle(height=1, width = 6)
        box.width = 4
        result.add(box)
        return result.scale(self.scale)
    
    def get_coord(self, index, dir=None):
        rect = self.items[index]

        if dir is not None:
            dot_prod_l = np.dot(dir,LEFT)
            dot_prod_r = np.dot(dir,RIGHT)
            tolerance = 1e-10
            if np.isclose(dot_prod_l,1,atol=tolerance):
                return rect.get_left() + 0.5 * rect.get_height() * LEFT
            elif np.isclose(dot_prod_r,1,atol=tolerance):
                return rect.get_right() + 0.5 * rect.get_height() * RIGHT
        else:
            return rect.get_center()