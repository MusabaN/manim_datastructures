from manim import *


class m_queue(VGroup):
    def __init__(self, queue=[], title="Queue", scale=1, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.len = ValueTracker(len(queue))
        self.scale = scale
        self.queue = queue
        self.title = Text(title)
        self.start_line = Line((0, 0, 0), (0, 1, 0)).scale(self.scale).next_to(self.title, RIGHT)
        self.prev = self.start_line

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
        new_elem = self.create_textbox(str(value), 30).next_to(self.prev, RIGHT, buff=0)
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
        if len(self.queue) == 0:
            return Succession(**kwargs)
        anims = []
        anim_group = []
        anims.append(FadeOut(self.queue[0], shift=LEFT))
        anims.append(self.queue[1].animate.next_to(self.start_line, RIGHT))
        anims.append(AnimationGroup(*anim_group, **kwargs))
        anims.append(Wait())
        self.remove(self.queue.pop(0))
        self.len -= 1
        return LaggedStart(*anims, **kwargs)

    def fade_out(self, **kwargs):
        anims = []
        for elem in self:
            anims.append(FadeOut(elem))
        anims.append(Wait())
        return LaggedStart(*anims, **kwargs)      
    
    def fade_in(self, **kwargs):
        anims = []
        for elem in self:
            anims.append(FadeIn(elem))
        anims.append(Wait())
        return LaggedStart(*anims, **kwargs)


if __name__ == "__main__":
    class theScene(Scene):
        def construct(self):
            queue = m_queue(queue=[1, 2, 3, 4, 5], title="Queue")
            self.add(queue)
            self.play(queue.enqueue(6, run_time=2, rate_func=linear))
            self.wait()
            self.play(queue.dequeue(run_time=2, rate_func=linear))
            self.wait()
            self.play(queue.fade_out(run_time=2, rate_func=linear))
            self.wait()
            self.play(queue.fade_in(run_time=2, rate_func=linear))
            self.wait()
    
    import os
    os.system("manim -p -ql ./m_queue.py theScene")
    input("Press Enter to continue...")
    os.system("rm -rf ./__pycache__")
    os.system("rm -rf ./media")