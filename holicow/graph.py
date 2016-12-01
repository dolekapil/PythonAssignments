"""
CSCI-603: Lab 9
Author: Sean Strout @ RIT CS
Author-1: Pratik kulkarni (psk7534@g.rit.edu)
Author-2: Kapil Dole (kmd1712@g.rit.edu)

An implementation of a graph data structure as an adjacency list.

Code taken from the online textbook and modified:

http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
"""

from vertex import Vertex

class Graph:
    """
    A graph implemented as an adjacency list of vertices.

    :slot: vertList (dict):  A dictionary that maps a vertex key to a Vertex
        object
    :slot: numVertices (int):  The total number of vertices in the graph
    """

    __slots__ = 'vertList', 'numVertices'

    def __init__(self):
        """
        Initialize the graph
        :return: None
        """
        self.vertList = []
        self.numVertices = 0

    def addVertex(self, vertex):
        """
        Add a new vertex to the graph.
        :param vertex: the vertex object.
        """
        # count this vertex if not already present
        if self.getVertex(vertex) == None:
            self.numVertices += 1
        self.vertList.append(vertex)


    def getVertex(self, vertex):
        """
        Retrieve the vertex from the graph.
        :param vertex: The vertex
        :return: Vertex if it is present, otherwise None
        """
        if vertex in self.vertList:
            return self.vertList[vertex]
        else:
            return None


    def addEdge(self, src, dest):
        """
        Add a new directed edge from a source to a destination of an edge cost.
        :param src: The source vertex identifier
        :param dest: The destination vertex identifier
        :return: None
        """
        if src not in self.vertList:
            self.addVertex(src)
        if dest not in self.vertList:
            self.addVertex(dest)
        src.addNeighbor(dest)

    def getVertices(self):
        """
        Return the list of vertex identifiers in the graph.
        :return: A list of vertex identifiers
        """
        return self.vertList

