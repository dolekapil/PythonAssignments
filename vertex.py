"""
CSCI-603: Graphs
Author: Sean Strout @ RIT CS

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
    """

    __slots__ = 'id', 'type', 'xCordinate', 'yCordinate', 'radius', 'connectedTo'

    def __init__(self, key, type, xCordinate, yCordinate, radius=None):
        """
        Initialize a vertex
        :param key: The identifier for this vertex
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
        Connect this vertex to a neighbor with a given weight (default is 0).
        :param nbr (Vertex): The neighbor vertex
        :param weight (int): The edge cost
        :return: None
        """
        self.connectedTo.append(nbr)