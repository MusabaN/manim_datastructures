from manim import *


class m_queue(VGroup):
    def __init__(self, queue=[], title="Queue", scale=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.scale = scale
        self.title = Text(title)
        self.start_line = Line((0, 0, 0), (0, 1, 0)).scale(self.scale).next_to(self.title, RIGHT)
        self.queue = [self.start_line]
        self.prev = self.queue[-1]


        self.add(self.title, self.start_line)
        for i in queue:
            self.enqueue_inner(i)
        
        

    
    def create_textbox(self, string, font_size, color=WHITE):
        result = VGroup()
        text = Text(string, font_size=font_size)
        box = Rectangle(stroke_color=color).surround(text)
        box.width = 2
        result.add(box, text)
        return result.scale(self.scale)

    def enqueue_inner(self, value):
        new_elem = self.create_textbox(str(value), 30).next_to(self.queue[-1], RIGHT, buff=0)
        
        # def update_func(m):
        #     for i in range(len(self.queue)):
        #         if self.queue[i] == m:
        #             m.next_to(self.queue[i-1], RIGHT, buff=0)
        #             return   # Exit the loop.

        # new_elem.add_updater(update_func)
        self.add(new_elem)
        self.queue.append(new_elem)
        self.prev = self.queue[-1]
        return new_elem


    def enqueue(self, value, **kwargs):
        anims = []
        new_elem = self.enqueue_inner(value)
        anims.append(FadeIn(new_elem, shift=LEFT))
        anims.append(Wait())
        return LaggedStart(*anims, 
            group=VGroup(new_elem),
            **kwargs)
    
    def dequeue(self, **kwargs):
        if len(self.queue) <= 1:
            return Succession(**kwargs)
        anims = []
        anims.append(FadeOut(self.queue[1], shift=LEFT))
        anims.append(Wait())
        for i in range(2, len(self.queue)):
            anims.append(self.queue[i].animate.next_to(self.queue[i-2], RIGHT, buff=0))
        self.remove(self.queue.pop(1))
        return AnimationGroup(*anims, **kwargs)

    def fade_out(self, **kwargs):
        anims = []
        for elem in self:
            anims.append(FadeOut(elem))
        anims.append(Wait())
        return AnimationGroup(*anims, **kwargs)      
    
    def fade_in(self, **kwargs):
        anims = []
        for elem in self:
            anims.append(FadeIn(elem))
        anims.append(Wait())
        return AnimationGroup(*anims, **kwargs)