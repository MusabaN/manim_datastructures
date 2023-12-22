from manim import *

class m_page_table(VGroup):
    def __init__(self,num_of_entries=6,title="Page table",scale = 1,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.scale = scale
        self.page = self.create_page(num_of_entries) 
        self.title = Text(title).scale(self.scale).next_to(self.page, UP)

        self.add(self.title,self.page)



    def create_page(self, num_of_entries):
        group = VGroup()
        if num_of_entries >= 1:
            first_box = self.create_text_box(30)
            group.add(first_box)
            prev = first_box
            for i in range (1,num_of_entries):
                new_elem = self.create_text_box(30).next_to(prev,DOWN,buff=0)
                group.add(new_elem)
                prev = new_elem
        
        return group

    def create_text_box(self, color=WHITE):
        result = VGroup()
        box = Rectangle(height=1, width = 6, color=color)
        box.width = 4
        result.add(box)
        return result.scale(self.scale)