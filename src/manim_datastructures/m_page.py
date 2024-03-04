from .m_abstract_memory import m_abstract_memory


class m_page(m_abstract_memory):
    def __init__(self, height=6, width=2, num_cells=4):
        super().__init__(height, width, num_cells)
