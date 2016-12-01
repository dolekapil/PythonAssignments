"""
CSCI-603: Lab 9
Author-1: Pratik kulkarni (psk7534@g.rit.edu)
Author-2: Kapil Dole (kmd1712@g.rit.edu)

This program takes file as a input using command line argument and which contains cows and paintball with their
x and y coordinate and radius if it is a paintball. We are creating graph with cows and paintball as vertices
and trying to trigger each paintball and checking how many cows are getting painted and returns the optimal
solution which is the paintball that colors maximum cows.
"""

import sys
import math
from vertex import Vertex
from graph import Graph

class Holicow:
    """
    This is implementation of HoliCow problem.

    :slot: verticesList (list):  A list that holds all vertices.
    :slot: numOfCowsPainted (dic):  The total number of cows painted after triggering
                                    each paint ball.
    :slot: finalResult (dic): The dictionary that holds optimal result.
    """

    __slots__ = 'verticesList', 'numOfCowsPainted', 'finalResult'

    def __init__(self):
        """
        Initializing HoliCow object.
        :return: None
        """
        self.verticesList = []
        self.numOfCowsPainted = {}
        self.finalResult = {}


    def processFile(self,argv):
        """
        This method process input file provided by the user and creates vertex objects
        for cow and paintball and throws error if incorrect file name provided or no
        command line arguments given.
        :param argv: command line argument (file name)
        :return: None
        """
        if len(sys.argv[1:]) == 1:
            file = sys.argv[1]
            try:
                fileHandle = open(file)
                for line in fileHandle:
                    line = line.strip()
                    data = line.split()
                    if data[0] == 'cow':
                        vertex = Vertex(data[1], data[0], data[2], data[3])
                        self.finalResult[data[1]] = []
                    else:
                        vertex = Vertex(data[1], data[0], data[2], data[3], data[4])
                    self.verticesList.append(vertex)
            except FileNotFoundError as e:
                print("File not found: ", file)
                sys.exit(0)
        else:
            print("Usage: python3 holicow.py {filename}")
            sys.exit(0)


    def buildGraph(self):
        """
        This method builds the graph, in short it creates adjacency list for each vertex
        in the graph.
        :return: Graph object.
        """
        holiCow = Graph()
        for vertex in self.verticesList:
            for x in self.verticesList:
                if vertex.type == 'paintball':
                    distance = math.sqrt((int(vertex.xCordinate)-int(x.xCordinate))**2 +
                                         (int(vertex.yCordinate)-int(x.yCordinate))**2)
                    if vertex.id != x.id and float(vertex.radius) >= distance:
                        holiCow.addEdge(vertex, x)
                if vertex not in holiCow.vertList:
                    holiCow.addVertex(vertex)
                if x not in holiCow.vertList:
                    holiCow.addVertex(x)
        return holiCow


    def displayField(self,fieldGraph):
        """
        It displays the field that should be displayed as an adjacency list where each vertex
        indicates what neighboring vertices it is connected to.
        :param fieldGraph: Graph object.
        :return: None
        """
        print('Field of Dreams')
        print('---------------')
        for vertex in fieldGraph.vertList:
            print(vertex)
        print()


    def triggerPaintball(self,fieldGraph):
        """
        This method trigger each starting paint ball in any order.
        :param fieldGraph: Graph object.
        :return: None
        """
        cowsPainted = False
        print('Beginning simulation...')
        for vertex in fieldGraph.vertList:
            counter = 0
            if vertex.type == 'paintball':
                visited = []
                visited.append(vertex.id)
                print('Triggering', vertex.id, 'paint ball...')
                for vertices in vertex.connectedTo:
                    if vertices.type == 'paintball':
                        counter = self.__triggerPaintball(vertex, vertices, counter, visited)
                    elif vertices.type == 'cow':
                        counter += 1
                        print('\t' + vertices.id + ' is painted ' + vertex.id + '!')
                if counter > 0:
                    cowsPainted = True
                self.numOfCowsPainted[vertex] = counter
        print()
        if not cowsPainted:
            print('Results:')
            print('No cows were painted by any starting paint ball!')
            sys.exit(0)


    def __triggerPaintball(self, triggeringPaintball, paintball, counter, visited):
        """
        This is recursive helper function for triggering each paintball.
        :param triggeringPaintball: Triggering paintball.
        :param paintball: Triggered paintball.
        :param counter: Counter for cows painted for each paintball triggering.
        :param visited: list containing visited nodes.
        :return: Counter for cows painted for each paintball triggering.
        """
        print('\t' + paintball.id + ' paint ball is triggered by ' + triggeringPaintball.id + ' paint ball')
        for vertex in paintball.connectedTo:
            if vertex.type == 'paintball' and vertex.id not in visited:
                visited.append(vertex.id)
                counter = self.__triggerPaintball(paintball, vertex, counter, visited)
            elif vertex.type == 'cow':
                counter += 1
                print('\t' + vertex.id + ' is painted ' + paintball.id + '!')
        return counter


    def displayOptimalResult(self):
        """
        This method is used for displaying optimal result, the paintball which colors cows
        the most.
        :return: None
        """
        optimalColors = []
        visited = []
        paintsOnCow = 0
        maximum = max(list(self.numOfCowsPainted.values()))
        for key, value in self.numOfCowsPainted.items():
            if value == maximum:
                optimalColors.append(key)
        for connectedVer in optimalColors[0].connectedTo:
            if connectedVer.type == 'cow':
                if optimalColors[0].id not in self.finalResult[connectedVer.id]:
                    tempList = self.finalResult[connectedVer.id]
                    tempList.append(optimalColors[0].id)
                    self.finalResult[connectedVer.id] = tempList
            else:
                visited.append(connectedVer.id)
                self.__displayOptimalResult(connectedVer, visited)
        print('Results:')
        for value in self.finalResult.values():
            paintsOnCow += len(value)
        print('Triggering the', optimalColors[0].id, 'paint ball is the best choice with',
              paintsOnCow, 'total paint on the cows:')
        for key, value in self.finalResult.items():
            print("\t" + key + "'s colors: {" + str(value).replace('[','').replace(']','') + "}")


    def __displayOptimalResult(self,paintball, visited):
        """
        This is recursive helper function which is used for displaying optimal result, the paintball
        which colors cows the most.
        :param paintball: Triggered paintball.
        :param visited: list of visited nodes
        :return: None
        """
        for vertics in paintball.connectedTo:
            if vertics.type == 'cow':
                if paintball.id not in self.finalResult[vertics.id]:
                    tempList = self.finalResult[vertics.id]
                    tempList.append(paintball.id)
                    self.finalResult[vertics.id] = tempList
            elif vertics.id not in visited:
                visited.append(vertics.id)
                self.__displayOptimalResult(vertics, visited)


def main(argv):
    """
    This is main function which takes file as commandline argument and make call
    to other helper functions.
    :param argv: command line argument (file)
    :return: None.
    """
    h = Holicow()
    h.processFile(argv)
    graphObj = h.buildGraph()
    h.displayField(graphObj)
    h.triggerPaintball(graphObj)
    h.displayOptimalResult()

if __name__ == '__main__':
    main(sys.argv)
