from manim import *


class m_virtual_address_element(VGroup):
    def __init__(self, num):
        super().__init__()
        self.num = num

        self.square = Square(1)
        self.integer = Integer(num).move_to(self.square.get_center())

        self.add(Square(1), Integer(num))

    def highlight(self, color):
        self[0].set_fill(color, opacity=0.5)

    def unhighlight(self):
        self[0].set_fill(BLACK, opacity=0)


class m_virtual_address(VGroup):
    
    def __init__(self, arr):
        super().__init__()

        elems = [m_virtual_address_element(i) for i in arr]

        for i in range(1, len(elems)):
            elems[i].next_to(elems[i-1], RIGHT, buff=0)

        self.add(*elems)

    def highlight(self, index, color):
        self[index].highlight(color)

    def unhighlight(self, index):
        self[index].unhighlight()


    def multi_highlight(self, start, end, color):
        for i in range(start, end):
            self.highlight(i, color)

    def multi_unhighlight(self, start, end):
        for i in range(start, end):
            self.unhighlight(i)

    # make indices version of multihighlight
    def multi_highlight_indices(self, indices, color):
        for i in indices:
            self.highlight(i, color)

    def multi_unhighlight_indices(self, indices):
        for i in indices:
            self.unhighlight(i)

    def popup_element(self, idx):
        self[idx].move_to(self[idx].get_center()+UP*0.25)

    def popdown_element(self, idx):
        self[idx].move_to(self[idx].get_center()+DOWN*0.25)