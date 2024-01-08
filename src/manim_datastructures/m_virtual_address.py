from manim import *

class m_virtual_address(VGroup):
    
    def __init__(self, arr):
        super().__init__()

        arr_ints = [Integer(i) for i in arr]
        arr_rects = [Square(1) for i in arr]

        for i in range(1, len(arr_rects)):
            arr_rects[i].next_to(arr_rects[i-1], RIGHT, buff=0)
            arr_ints[i].move_to(arr_rects[i].get_center())

        self.add(*arr_rects, *arr_ints)