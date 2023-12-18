from importlib import resources

def get_svg_path(file_name):
    svg_files_path = resources.files('manim_datastructures.svg')
    return svg_files_path / file_name