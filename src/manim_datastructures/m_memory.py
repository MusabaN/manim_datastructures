from manim import *

class m_memory(VGroup):


    def __init__(self,table=[],number = 0, title = "Memory", scale = 1, *args, **kwargs):
         
        super().__init__(*args,**kwargs) 
        self.scale = scale
        self.top_line = Line(LEFT, RIGHT).scale(self.scale)
        self.title = Text(title).scale(self.scale).next_to(self.top_line, UP)
        self.stack = []
        self.val_stack = []
        self.prev = self.top_line

        self.add(self.title, self.top_line)
        
        if number and not table:
            for i in range (0,number):
                self.push_inner(i)

        if number and table:
            for i in range (0,number):
                if i<len(table):
                    self.push_inner(i,value=table[i])
                else:
                    self.push_inner(number=i)
        


    def create_textbox(self, font_size,number, string=None, color=WHITE):
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
        if string:
            text = Text(string, font_size=font_size)
            box = Rectangle(stroke_color=color).surround(text)
        else:
            box = Rectangle(stroke_color=color)
        box.width = 4
        box.height = 1
        nmb = Text(number, font_size=font_size).next_to(box,LEFT,buff = 0.1)
        if string:
            result.add(box, text,nmb)
        else:
            result.add(box,nmb)    

        return result.scale(self.scale)
        
    
    def push_inner(self, number, value=None):
        """
        Pushes an element to the stack without an animation.

        Parameters:
        value (str): The value to be pushed onto the stack.

        Returns:
        Group: A group of textbox and text representing the new element.
        """
        self.val_stack.append(value)
        if value:
            new_elem = self.create_textbox(30,str(number), str(value)).next_to(self.prev, DOWN, buff=0)
        else:
            new_elem = self.create_textbox(30,str(number)).next_to(self.prev, DOWN, buff=0)

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
        anims.append(Wait())
        return LaggedStart(*anims, 
            group=VGroup(new_elem),
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
        
        self.val_stack.pop()
        anims = []
        anims.append(FadeOut(self.stack[-1], shift=DOWN))
        anims.append(Wait())
        self.remove(self.stack.pop())
        if len(self.stack) > 0:
            self.prev = self.stack[-1]
        else:
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
    
