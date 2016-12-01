__author__ = 'dolek'

import sys
import math
from vertex import Vertex
from graph import Graph

def buildGraph(verticesList):
    holiCow = Graph()
    for vertex in verticesList:
        if vertex.type == 'paintball':
            for x in verticesList:
                distance = math.sqrt((int(vertex.xCordinate)-int(x.xCordinate))**2 +
                                     (int(vertex.yCordinate)-int(x.yCordinate))**2)
                if vertex.id != x.id and float(vertex.radius) >= distance:
                    holiCow.addEdge(vertex, x)
    return holiCow

def processFile(argv):
    verticesList = []
    if len(sys.argv[1:]) == 1:
        file=sys.argv[1]
        try:
            fileHandle = open(file)
            for line in fileHandle:
                line = line.strip()
                data = line.split()
                if data[0] == 'cow':
                    vertex = Vertex(data[1], data[0], data[2], data[3])
                else:
                    vertex = Vertex(data[1], data[0], data[2], data[3], data[4])
                verticesList.append(vertex)
            return verticesList
        except FileNotFoundError as e:
            print("File not found: ", file)
            sys.exit(0)
    else:
        print("Usage: python3 holicow.py {filename}")
        sys.exit(0)

def displayField(fieldGraph):
    print('Field of Dreams')
    print('---------------')
    for vertex in fieldGraph.vertList:
        print(vertex)
    print()

def triggerPaintball(fieldGraph):
    result = {}
    donePaintBall = []
    cowsPainted = False
    print('Beginning simulation...')
    for vertex in fieldGraph.vertList:
        counter = 0
        if vertex.type == 'paintball':
            donePaintBall.append(vertex.id)
            print('Triggering ', vertex.id, ' paint ball...')
            for vertices in vertex.connectedTo:
                if vertices.type == 'paintball':
                    counter = __triggerPaintball(vertex, vertices, counter, donePaintBall)
                else:
                    counter +=1
                    print('\t',vertices.id,' is painted ',vertex.id,'!')
            if counter > 0:
                cowsPainted = True
            result[vertex] = counter
    print()
    if not cowsPainted:
        print('Results:')
        print('No cows were painted by any starting paint ball!')
        sys.exit(0)
    return result

def __triggerPaintball(triggeringPaintball, paintball, counter, donePaintBall):
    print('\t', paintball.id, ' paint ball is triggered by ', triggeringPaintball.id, ' paint ball')
    for vertex in paintball.connectedTo:
        if vertex.type == 'paintball' and vertex.id not in donePaintBall:
            donePaintBall.append(vertex.id)
            __triggerPaintball(paintball, vertex, counter, donePaintBall)
        elif vertex.type == 'cow':
            counter +=1
            print('\t',vertex.id,' is painted ',paintball.id,'!')
    return counter

def displayOptimalResult(results, verticesList):
    optimalResult = {}
    optimalColor = []
    donePaintBall = []
    paintsOnCow = 0
    for vertex in verticesList:
        if vertex.type == 'cow':
            optimalResult[vertex.id] = []

    maximum = max(list(results.values()))
    for key, value in results.items():
        if value == maximum:
            optimalColor.append(key)

    for connectedVer in optimalColor[0].connectedTo:
        if connectedVer.type == 'cow':
            tempList = optimalResult[connectedVer.id]
            tempList.append(optimalColor[0].id)
            optimalResult[connectedVer.id]=tempList
        else:
            donePaintBall.append(connectedVer.id)
            optimalResult =__displayOptimalResult(connectedVer, optimalResult, donePaintBall)

    print('Results:')
    for value in optimalResult.values():
        paintsOnCow += len(value)
    print('Triggering the ', optimalColor[0].id, ' paint ball is the best choice with',
          paintsOnCow,'total paint on the cows:')
    for key, value in optimalResult.items():
        print("\t", key, "'s colors: {", str(value).replace('[','').replace(']',''), "}")


def __displayOptimalResult(paintball, optimalResult, donePaintBall):
    for vertics in paintball.connectedTo:
        if vertics.type == 'cow':
            tempList = optimalResult[vertics.id]
            tempList.append(paintball.id)
            optimalResult[vertics.id] = tempList
        elif vertics.id not in donePaintBall:
            donePaintBall.append(vertics.id)
            __displayOptimalResult(vertics, optimalResult, donePaintBall)
    return optimalResult

def main(argv):
    verticesList = processFile(argv)
    holiCow = buildGraph(verticesList)
    displayField(holiCow)
    results = triggerPaintball(holiCow)
    displayOptimalResult(results, verticesList)

if __name__ == '__main__':
    main(sys.argv)
