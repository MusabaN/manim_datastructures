from manim import *

class m_stack(VGroup):
    """ 
    A class used to illustrate a stack.

    Attributes
    ----------
    scale : float
        a scaling factor for the images
    title : str
        title of the stack
    stack : list
        a list containing all stack elements
    ...

    Methods
    -------
    create_textbox(string, font_size, color=WHITE):
        Creates a nice textbox
    create_pointers()
        Creates pointers for the stack
    push_inner(value):
        Pushes an element to the stack without animations
    push(value, **kwargs):
        Pushes an element to the stack with animations
    pop(**kwargs):
        Pops an element from the stack with animations
    fade_out(**kwargs):
        Fades out all elements in the stack
    fade_in(**kwargs):
        Fades in all elements in the stack
    """

    def __init__(self, table=[], scale=1, title="Stack", *args, **kwargs):
        """
        Parameters:
        table (list, optional): A list of initial values. 
        scale (float, optional): The scaling factor of the stack and its elements. Defaults to 1.
        title (str, optional): The title of the stack. Defaults to 'Stack'.
        """
        super().__init__(*args, **kwargs)
        self.scale = scale
        self.top_line = Line(LEFT, RIGHT).scale(self.scale)
        self.title = Text(title).scale(self.scale).next_to(self.top_line, UP)
        self.bp = self.create_pointers([LEFT, RIGHT], "BP")
        self.sp = self.create_pointers([RIGHT, LEFT], "SP")
        self.stack = []
        self.prev = self.top_line

        self.add(self.title, self.top_line, self.bp, self.sp)
        for i in table:
            self.push_inner(i)
        
        if (len(table) > 0):
            self.sp.next_to(self.stack[-1], RIGHT)


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
        
    
    def create_pointers(self, direction, name):
        """
        Creates pointers for the stack.

        Parameters:
        direction (list): A list of two positions indicating the direction of the pointers.
        name (str): The label of the pointer.

        Returns:
        VGroup: A group of pointer and text.
        """
        pointer = Arrow(start=direction[0], end=direction[1], stroke_width=3, buff=0.5).scale(self.scale, scale_tips=True).next_to(self.top_line, direction[0])
        text = Text(name, font_size=30).scale(self.scale).next_to(pointer, direction[0])
        return VGroup(pointer, text)
    
    def push_inner(self, value):
        """
        Pushes an element to the stack without an animation.

        Parameters:
        value (str): The value to be pushed onto the stack.

        Returns:
        Group: A group of textbox and text representing the new element.
        """
        new_elem = self.create_textbox(str(value), 30).next_to(self.prev, DOWN, buff=0)
        self.add(new_elem)
        self.stack.append(new_elem)
        self.prev = self.stack[-1]
        return new_elem
    
    def push(self, value, **kwargs):
        """
        Pushes an element to the stack with an animation.

        Parameters:
        value (str): The value to be pushed onto the stack.
        **kwargs: Variable length argument list to support any number of animations.

        Returns:
        AnimationGroup: A group of animations for the operation of pushing onto the stack.
        """
        anims = []
        new_elem = self.push_inner(value)
        anims.append(FadeIn(new_elem, shift=UP))
        anims.append(self.sp.animate.next_to(new_elem, RIGHT))
        anims.append(Wait())
        return LaggedStart(*anims, 
            group=VGroup(new_elem, self.sp),
            **kwargs)
    
    def pop(self, **kwargs):
        """
        Pops an element from the stack with an animation.

        **kwargs: Variable length argument list to support any number of animations.

        Returns:
        AnimationGroup: A group of animations for the operation of popping from the stack.
        """
        if len(self.stack) == 0:
            return Succession(**kwargs)
        anims = []
        anims.append(FadeOut(self.stack[-1], shift=DOWN))
        anims.append(Wait())
        self.remove(self.stack.pop())
        if len(self.stack) > 0:
            anims.append(self.sp.animate.next_to(self.stack[-1], RIGHT))
            self.prev = self.stack[-1]
        else:
            anims.append(self.sp.animate.next_to(self.top_line, RIGHT))
            self.prev = self.top_line
        return LaggedStart(*anims, **kwargs)
    
    def fade_out(self, **kwargs):
        """
        Fades out all elements in the stack.

        **kwargs: Variable length argument list to support any number of animations.

        Returns:
        AnimationGroup: A group of animations for fading out all the stack elements.
        """
        anims = []
        for elems in self:
            anims.append(FadeOut(elems))
        return AnimationGroup(*anims, **kwargs)
    
    def fade_in(self, **kwargs):
        """
        Fades in all elements in the stack.

        **kwargs: Variable length argument list to support any number of animations.

        Returns:
        AnimationGroup: A group of animations for fading in all the stack elements.
        """
        anims = []
        for elems in self:
            anims.append(FadeIn(elems))
        return AnimationGroup(*anims, **kwargs)
