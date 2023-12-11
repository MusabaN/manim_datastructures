from manim import *

class m_table(VGroup):
    """ 
    A class used to describe a m_table object.

    ...

    Attributes
    ----------
    scale: int
        a scaling factor
    data: dict
        a dictionary containing key value pairs
    title: str
        title of the table

    Methods
    -------
    set(register,value):
        Updates the value of a given register
    unset(register):
        Removes a register from the table
    update_table():
        Redraws the table with current data
    animate_change(register, value, **kwargs):
        Creates a sequence of animations highlighting a change in the table
    highlight_cell(register, **kwargs):
        Creates a sequence of animations highlighting a specific cell in the table
    """

    def __init__(self, data, title="Table",scale=1, *args, **kwargs):
        """
        Parameters:
        data (dict): A dictionary containing key-value pairs.
        title (str, optional): The title of the table. Defaults to 'Table'.
        scale (int, optional): The scaling factor of the table. Defaults to 1.
        """
        super().__init__(*args, **kwargs)
        self.scale = scale
        self.data = data
        self.table_title = Text(str(title)).scale(self.scale)
        self.update_table()

    def set(self, register, value):
        """
        Sets the value of the specified register.

        Parameters:
        register (str/int): The register whose value is to be set.
        value (str/int/float): The value to be set.
        """
        self.data[register] = value
        self.update_table()

    def unset(self, register):
        """
        Removes the specified register from the table.

        Parameters:
        register (str/int): The register to be removed.
        """
        del self.data[register]
        self.update_table()

    def update_table(self):
        """Updates and redraws the table with the current data."""
        self.con_table = [[s, f"0x{n:03x}"] for s, n in self.data.items()]
        self.table = Table(self.con_table, include_outer_lines=True).scale(self.scale)
        self.table_title.next_to(self.table, UP)
        self.become(VGroup(self.table_title, self.table).move_to(self.get_center()))

    def animate_change(self, register, value, color=ORANGE, **kwargs):
        """
        Creates a sequence of animations highlighting a change in the table.

        Parameters:
        register (str/int): The register whose value has changed.
        value (str/int/float): The new value of the register.

        Returns:
        Succession: A sequence of animations for Manim to play.

        """
        self.update_table()
        anims = []
        index = list(self.data.keys()).index(register)+1
        self.table.add_highlighted_cell((index, 0), color=color)
        self.table[0].set_z_index(-1).set_opacity(0)
        anims.append(self.table[0].animate.set_opacity(1).build())
        anims.append(Wait())
        anims.append(self.animate.set(register, value))
        anims.append(Wait())
        anims.append(self.table[0].animate.set_opacity(0).build())
        return Succession(*anims, **kwargs)

    def highlight_cell(self, register, color=GREEN, **kwargs):
        """
        Creates a sequence of animations highlighting a specific cell in the table.

        Parameters:
        register (str/int): The register to be highlighted.

        Returns:
        Succession: A sequence of animations for Manim to play.

        """
        self.update_table()
        anims = []
        index = list(self.data.keys()).index(register)+1
        self.table.add_highlighted_cell((index, 0), color=color)
        self.table[0].set_z_index(-1).set_opacity(0)
        anims.append(self.table[0].animate.set_opacity(1).build())
        anims.append(Wait())
        anims.append(self.animate.set(register, self.data[register]))
        anims.append(Wait())
        anims.append(self.table[0].animate.set_opacity(0).build())
        return Succession(*anims, **kwargs)
