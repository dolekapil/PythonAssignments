"""
CSCI-603: Lab 9
Author: Sean Strout @ RIT CS
Author-1: Pratik kulkarni (psk7534@g.rit.edu)
Author-2: Kapil Dole (kmd1712@g.rit.edu)
An implementation of a vertex as part of a graph.

Code taken from the online textbook and modified:

http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
"""

class Vertex:
    """
    An individual vertex in the graph.

    :slots: id:  The identifier for this vertex (user defined, typically
        a string)
    :slots: connectedTo:  A dictionary of adjacent neighbors, where the key is
        the neighbor (Vertex), and the value is the edge cost (int)
    :slots: type: the type of the vertex(cow or paintball).
    :slots: xCordinate: The x coordinate of the vertex.
    :slots: yCordinate: The y coordinate of the vertex.
    :slots: radius: range of the paintball.
    """

    __slots__ = 'id', 'type', 'xCordinate', 'yCordinate', 'radius', 'connectedTo'

    def __init__(self, key, type, xCordinate, yCordinate, radius=None):
        """
        Initialize a vertex
        :param key: The identifier for this vertex
        :param type: the type of the vertex
        :param xCordinate: the x coordinate of the vertex.
        :param yCordinate: the y coordinate of the vertex.
        :param radius: the range of the paintball.
        :return: None
        """
        self.id = key
        self.type = type
        self.xCordinate = xCordinate
        self.yCordinate = yCordinate
        self.radius = radius
        self.connectedTo = []

    def __str__(self):
        """
        Return a string representation of the vertex and its direct neighbors:

            vertex-id connectedTo [neighbor-1-id, neighbor-2-id, ...]

        :return: The string
        """
        return str(self.id) + ' connectedTo: ' + str([str(x.id) for x in self.connectedTo])

    def addNeighbor(self, nbr):
        """
        Connect this vertex to a neighbor.
        :param nbr (Vertex): The neighbor vertex
        :return: None
        """
        self.connectedTo.append(nbr)