from manim import *
import test_setup
from manim_datastructures import *

class theScene(Scene):
        def construct(self):
            queue = m_queue(scale=0.5).to_edge(LEFT)
            self.play(queue.fade_in())
            self.play(queue.enqueue(6, run_time=0.2, rate_func=linear))
            self.wait()
            self.play(queue.enqueue(6, run_time=0.2, rate_func=linear))
            self.wait()
            self.play(queue.enqueue(6, run_time=0.2, rate_func=linear))
            self.wait()
            self.play(queue.dequeue(run_time=0.2, rate_func=linear))
            self.wait()
            self.play(queue.dequeue(run_time=0.2, rate_func=linear))
            self.wait()
            self.play(queue.dequeue(run_time=0.2, rate_func=linear))
            self.wait()
            self.play(queue.enqueue(6, run_time=0.2, rate_func=linear))
            self.wait()
            self.play(queue.enqueue(6, run_time=0.2, rate_func=linear))
            self.wait()
            self.play(queue.enqueue(6, run_time=0.2, rate_func=linear))
            self.wait()
            self.play(queue.dequeue(run_time=0.2, rate_func=linear))
            self.wait()
            self.play(queue.dequeue(run_time=0.2, rate_func=linear))
            self.wait()
            self.play(queue.dequeue(run_time=0.2, rate_func=linear))
            self.wait()