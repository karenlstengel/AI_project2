from array import *
"""script for for main"""
'''import CSP
import Maze
import sys

if __name__ == "__main__":
    print("hello world")
    file = str(sys.argv[1])

    with open(file) as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]

    dim = len(lines[0])
    dim2 = len(lines)
    print(dim)
    print(dim2)
    graph = ""
    for l in lines:
        graph = graph + l'''


def includesSquare(symbol, squareList):
    count = 0
    for i in squareList:
        if i.symbol == symbol:
        #squareList.remove(i)
            count += 1
    return count

class Square:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y

class Graph:
    def __init__(self, inString, x, y):
        self.graph = []
        self.xdim = x
        self.ydim = y
        self.colors = set(())
        k = 0
        end = len(inString) - 1
        for i in range(x):
            line = []
            for j in range(y):
                if k <= end:
                    line.append(Square(inString[k], i, j))
                    if inString[k] not in self.colors:
                        self.colors.add(inString[k])
                    k += 1
            self.graph.append(line)
        self.colors.remove("_")
        
    def solvePuzzleDumb(self):
        if self.solveSquare(0, 0):
            return self.graph
        else:
            print("No solution.")
            
    def solveSquare(self, x, y):
        done = False
        nextSquare = self.getNext(x, y)
        if nextSquare is None:
            return True
        elif self.graph[x][y] != "_":
            done = self.solveSquare(nextSquare[0], nextSquare[1])
        else:
            options = set(())
            for i in self.colors:
                options.add(i.lower())
            for i in options:
                self.graph[x][y].symbol = i
                valid = self.checkConstraints(x, y)
                if valid:
                    done = self.solveSquare(nextSquare[0], nextSquare[1])
                    if done == True:
                        break
            if done == False:
                self.graph[x][y].symbol = '_'
        return done
            
    def findNeighbors(self, x, y):
        nbors = list(())
        nbors.append(self.graph[x][y])
        if(x > 0):
            nbors.append(self.graph[x-1][y])
        if(y > 0):
            nbors.append(self.graph[x][y-1])
        if(x < self.xdim - 1):
            nbors.append(self.graph[x+1][y])
        if(y < self.ydim - 1):
            nbors.append(self.graph[x][y+1])
        return nbors
    
    def checkConstraints(self, x, y):
        i = self.graph[x][y].symbol #symbol we're testing
        if i != "_": 
            return False
        valid = True
        nbors = self.findNeighbors(x, y)
        nbors.append(self.graph[x][y])
        
        for j in nbors:
            cnbors = self.findNeighbors(j.x, j.y)
            if j.symbol.isupper(): #Make sure endpoints don't have more than one matching color coming out of them and that if it doesn't have any, that it has at least one blank adjacent square
                symbolCount = inludesSquare(j.symbol.lower(), cnbors)
                blankCount = includesSquare("_", cnbors)
                if symbolCount > 1:
                    valid = False
                if blankCount == 0 and symbolCount != 1:
                    valid = False
            else: #Symbol is not an endpoint
                symbolCount = includesSquare(j.symbol, cnbors)
                blankCount = includesSquare("_", cnbors)
                if symbolCount > 2:
                    valid = False
                if symbolCount == 1 and blankCount < 1:
                    valid = False
                if symbolCount == 0 and blankCount < 2:
                    valid = False
        return valid
                    
    def getNext(self, x, y):
        if x == self.xdim - 1 and y == self.ydim - 1:
            return None
        elif x == self.xdim - 1:
            return [0, y + 1]
        else:
            return [x + 1, y]
    
    def printGraph(self):
        for i in range(self.xdim):
            line = ""
            for j in range(self.ydim):
                line += self.graph[i][j].symbol
            print(line)
        

g5x5 = Graph("B__RO___Y___Y___RO_G_BG__", 5, 5)
g7x7 = Graph("___O____B__GY____BR_____Y____________R____G___O__", 7, 7)
g8x8 = Graph("___R__G__BYP_______O_GR____P__________Y_____BOQ__Q______________", 8, 8)
g9x9 = Graph("D__BOK_____O__R_____RQ__Q__DB________G__________P____G__Y___Y________KP__________", 9, 9)
g10x10 = Graph("RG____________O___O__YP_Q___Q_____________G_____________R_________B___P__________Y______B___________", 10, 10)
g12x12 = Graph("_____________________________K_Y_G_____Y___G_____O_P______Q____R_OQ_________P_ARK____D__D_W_______________W___B_______B__________A_____________", 12, 12)
g14x14 = Graph("_______________B___A______________W____RP_D____A__W____________OB____G_OY______K_____________D____G___________________R_Y___________Q_______________________QP_______________K______________________", 14, 14)
g5x5.printGraph()
g5x5.solvePuzzleDumb()
g5x5.printGraph()
'''
g5x5.printGraph()
g5x5.getOptions(3, 3)
g7x7.printGraph()
g7x7.getOptions(4, 4)
g14x14.printGraph()
g14x14.getOptions(7, 7)'''
