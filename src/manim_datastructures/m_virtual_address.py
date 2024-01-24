from manim import *

class m_virtual_address_bracket(VGroup):
    def __init__(self):
        super().__init__()
        self.bracket = BraceBetweenPoints(ORIGIN, RIGHT*2, UP).set_fill(WHITE, opacity=0)
        self.add(self.bracket)

    def update_bracket_points(self, start, end, direction):
        self[0] = BraceBetweenPoints(start, end, direction).set_fill(
            WHITE,
            opacity=self[0].get_fill_opacity()
        )

    def show_bracket(self):
        self[0].set_fill(WHITE, opacity=1)

    def hide_bracket(self):
        self[0].set_fill(WHITE, opacity=0)


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

    def get_top_corner(self, direction):
        return self[0].get_critical_point(UP + direction)


class m_virtual_address(VGroup):
    
    def __init__(self, arr):
        super().__init__()

        elems = [m_virtual_address_element(i) for i in arr]

        for i in range(1, len(elems)):
            elems[i].next_to(elems[i-1], RIGHT, buff=0)

        self.bracket = m_virtual_address_bracket()
        self.add(*elems, self.bracket)

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

    def multi_popup(self, start, end):
        for i in range(start, end):
            self.popup_element(i)

    def multi_popdown(self, start, end):
        for i in range(start, end):
            self.popdown_element(i)

    def multi_popup_indices(self, indices):
        for i in indices:
            self.popup_element(i)

    def multi_popdown_indices(self, indices):
        for i in indices:
            self.popdown_element(i)

    def set_bracket_points(self, start, end, direction=UP):
        self.bracket.update_bracket_points(
            self[start].get_top_corner(LEFT),
            self[end].get_top_corner(RIGHT),
            direction
        )

    def show_bracket(self):
        self[-1].show_bracket()

    def hide_bracket(self):
        self[-1].hide_bracket()

    def get_coord(self, index, corner):
        return self[index].get_corner(corner)
