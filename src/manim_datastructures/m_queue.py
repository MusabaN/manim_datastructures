from manim import *


class m_queue(VGroup):
    """ 
    A class used to illustrate a queue.

    Attributes
    ----------
    scale : float
        a scaling factor for the images
    title : str
        title of the queue
    queue : list
        a list containing all queue elements
    ...

    Methods
    -------
    create_textbox(string, font_size, color=WHITE):
        Creates a nice textbox
    enqueue_inner(value):
        Enqueues an element to the queue without animations
    enqueue(value, **kwargs):
        Enqueues an element to the queue with animations
    dequeue(**kwargs):
        Dequeues an element from the queue with animations
    fade_out(**kwargs):
        Fades out all elements in the queue
    fade_in(**kwargs):
        Fades in all elements in the queue
    """

    def __init__(self, queue=[], title="Queue", scale=1, *args, **kwargs):
        """
        Parameters:
        queue (list, optional): A list of initial values. 
        scale (float, optional): The scaling factor of the queue and its elements. Defaults to 1.
        title (str, optional): The title of the queue. Defaults to 'Queue'.
        """
        super().__init__(*args, **kwargs)
        self.scale = scale
        self.title = Text(title).scale(self.scale)
        self.start_line = Line((0, 0, 0), (0, 1, 0)).scale(self.scale).next_to(self.title, RIGHT)
        self.queue = [self.start_line]
        self.prev = self.queue[-1]


        self.add(self.title, self.start_line)
        for i in queue:
            self.enqueue_inner(i)
        
        

    
    def create_textbox(self, string, font_size, color=WHITE):
        """
        Creates a textbox with the given parameters.

        Parameters:
        string (str): The string to be set in the textbox.
        font_size (int): The font size of the text in the textbox.
        color (RGB/str, optional): The color of the textbox. Defaults to WHITE.

        Returns:
        VGroup: A group of objects (textbox and text) representing a "textbox".
        """

        result = VGroup()
        text = Text(string, font_size=font_size)
        box = Rectangle(stroke_color=color).surround(text)
        box.width = 2
        result.add(box, text)
        return result.scale(self.scale)

    def enqueue_inner(self, value):
        """
        Enqueues an element to the queue without an animation.

        Parameters:
        value (str): The value to be enqueued onto the queue.

        Returns:
        VGroup: A group of textbox and text representing the new element.
        """

        new_elem = self.create_textbox(str(value), 30).next_to(self.queue[-1], RIGHT, buff=0)
        self.add(new_elem)
        self.queue.append(new_elem)
        self.prev = self.queue[-1]
        return new_elem


    def enqueue(self, value, **kwargs):
        """
        Enqueues an element to the queue with an animation.

        Parameters:
        value (str): The value to be enqueued onto the queue.
        **kwargs: Variable length argument list to support any number of animations.

        Returns:
        AnimationGroup: A group of animations for the operation of enqueuing onto the queue.
        """
        
        anims = []
        new_elem = self.enqueue_inner(value)
        anims.append(FadeIn(new_elem, shift=LEFT))
        anims.append(Wait())
        return LaggedStart(*anims, 
            group=VGroup(new_elem),
            **kwargs)
    
    def dequeue(self, **kwargs):
        """
        Dequeues an element from the queue with an animation.

        **kwargs: Variable length argument list to support any number of animations.

        Returns:
        AnimationGroup: A group of animations for the operation of dequeuing from the queue.
        """

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
        """
        Fades out all elements in the queue.

        **kwargs: Variable length argument list to support any number of animations.

        Returns:
        AnimationGroup: A group of animations for fading out all the queue elements.
        """

        anims = []
        for elem in self:
            anims.append(FadeOut(elem))
        anims.append(Wait())
        return AnimationGroup(*anims, **kwargs)      
    
    def fade_in(self, **kwargs):
        """
        Fades in all elements in the queue.

        **kwargs: Variable length argument list to support any number of animations.

        Returns:
        AnimationGroup: A group of animations for fading in all the queue elements.
        """

        anims = []
        for elem in self:
            anims.append(FadeIn(elem))
        anims.append(Wait())
        return AnimationGroup(*anims, **kwargs)