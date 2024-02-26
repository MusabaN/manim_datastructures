"""
This file contains the m_orthogonal_line class, which is a subclass of the Line class.
Original code provided from Abulafia on the manim discord server. Not written my me, Ole Jørgen Norstrand, the author of this project.
"""

from manim import *


class m_orthogonal_line(Line):
    """Creates a polyline that goes from p1 to p2, composed
    only by horizontal and vertical segments. The shape of the
    line is controlled by the path parameter.

    There are two ways to use this class:

    1. p1 and p2 are the start and end points of the line, and
       path is a string with the characters "-" and "|"  indicating
       the horizontal and vertical segments of the line.

       For example "-|-" will start with a horizontal segment, that
       will go until the x coordinate intermediate between p1 and p2,
       then a vertical segment up to the y coordinate of p2, and finally
       a horizontal segment to p2.

       If several "-" or "|" are used, each one represent a
       fraction of the total distance to be covered. For example "--|-"
       will make the vertical segment to be a 2/3 in horizontal
       distance from p1 to p2, because "--|-" contains 3 "-" segments.

    2. p2 is omitted and path is a list of tuples (p, s) where p is
       a point and s is a string with the characters "-" and "|" as
       in the previous case. In this case a line is created from p1
       to p, following the path in s, and the procedure is repeated
       for the next tuple in the list, until the list is exhausted.
       The final point of the polyline is the last p in the list.

    The class returns a Line object that contains several segments
    """

    def __init__(self, p1, p2=None, path=None, **kwargs):
        if p2 is None:
            if path is None:
                p2 = p1
                path = [(p2, "-|")]
            elif type(path) == str:
                p2 = p1
                path = [(p2, path)]
            else:
                p2 = path[-1][0]
        if type(path) == str:
            path = [(p2, path)]
        super().__init__(p1, p2, **kwargs)
        self.add_corners(path)

    def add_corners(self, path):
        last_visited = self.get_start()
        vertices = [last_visited]
        for dst, p in path:
            num_horiz = p.count("-")
            num_vert = p.count("|")
            start = last_visited
            end = dst
            x_length = end[0] - start[0]
            y_length = end[1] - start[1]
            for c in p:
                vertex = vertices[-1].copy()
                if c == "-":
                    vertex[0] += x_length / num_horiz
                elif c == "|":
                    vertex[1] += y_length / num_vert
                vertices.append(vertex)
            last_visited = dst
        self.set_points_as_corners(vertices)

    def midpoint(self, segment=-1):
        """Returns a point on the polyline. If segment is given, it
        returns the midpoint of the segment (numbered from 0),
        otherwise it returns the midpoint of the whole polyline.
        Each segment corresponds to a "-" or "|" in the path string.
        """
        if segment >= 0:
            vertices = self.get_anchors()
            if segment * 2 + 1 < len(vertices):
                return (vertices[segment * 2] + vertices[segment * 2 + 1]) / 2
        return self.point_from_proportion(0.5)
