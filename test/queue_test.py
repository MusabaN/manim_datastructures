from manim import *
import test_setup
from manim_datastructures import *

class theScene(Scene):
        def construct(self):
            queue = m_queue()
            self.add(queue)
            self.play(queue.enqueue(6, run_time=2, rate_func=linear))
            self.wait()
            self.play(queue.enqueue(6, run_time=2, rate_func=linear))
            self.wait()
            self.play(queue.enqueue(6, run_time=2, rate_func=linear))
            self.wait()
            self.play(queue.dequeue(run_time=2, rate_func=linear))
            self.wait()
            self.play(queue.fade_out(run_time=2, rate_func=linear))
            self.wait()
            self.play(queue.fade_in(run_time=2, rate_func=linear))
            self.wait()