import os
import sys
from manim import Code
from manim.mobject.text.text_mobject import remove_invisible_chars


def get_resource_path(relative_path):
    """Get the absolute path to the resource, works for dev and for PyInstaller"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def create_code(file_name):
    """Create a Code object from a file"""
    # get the absolute path from where the script is run
    # and append the relative path to the code example
    base_path = os.getcwd()
    filepath = os.path.join(base_path, file_name)
    
    return \
        remove_invisible_chars(
            Code(file_name=filepath)
        )