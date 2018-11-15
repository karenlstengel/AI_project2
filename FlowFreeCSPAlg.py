from array import *
import time
import sys
from queue import PriorityQueue

def includesSquare(symbol, squareList): #counts the number of occurrences of a symbol in a list of squares
    count = 0
    for i in squareList:
        if i.symbol == symbol:
            count += 1
    return count

class Square:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y
        self.constrained = 0

class Graph:
    def __init__(self, inString, x, y):
        self.graph = [] #double array of squares
        self.xdim = x #x-dimension
        self.ydim = y #y-dimension
        self.colors = set(()) #all colors included in the graph
        self.eCount = 0
        k = 0
        end = len(inString) - 1
        for i in range(x): #build graph from string
            line = []
            for j in range(y):
                if k <= end:
                    line.append(Square(inString[k], i, j))
                    if inString[k] not in self.colors:
                        self.colors.add(inString[k])
                    k += 1
            self.graph.append(line)
        self.colors.remove("_") #remove blank squares
        self.squaresByConst = PriorityQueue()
        self.count = 0
        self.options = set(())
        for i in self.colors: #create a list of lower case colors available
            self.options.add(i.lower())

    def getConstrained(self, square):
        return square.constrained

    def solvePuzzleDumb(self):
        self.count = 0
        print("Unsolved Puzzle:")
        self.printGraph()
        if self.solveSquare(0, 0, "dumb"):
            print("Solution:")
            self.printGraph()
            #return self.graph
        else:
            print("No solution.")
        print("Assignments made: " + str(self.count))

    def makeQueue(self):
        #set constraints and set up max priority queue
        if self.squaresByConst.qsize() > 0:
            self.squaresByConst = PriorityQueue()
        for i in range(self.xdim):
            for j in range(self.ydim):
                if self.graph[i][j].symbol == "_":
                    self.graph[i][j].constrained = self.howConstrained(self.graph[i][j], self.findNeighbors(i, j))
                    priorityNum = -self.graph[i][j].constrained
                    self.squaresByConst.put(((priorityNum, self.eCount), self.graph[i][j])) #set up as max priority queue instead of min
                    self.eCount = self.eCount + 1

    def countColors(self, nbors, options):
        temp = list()
        counts = PriorityQueue()
        reordered = list()
        for x in nbors:
            temp.append(x.symbol.lower())
        #print(temp)
        for x in options:
            counts.put((-temp.count(x), x))
        while not counts.empty():
            hi = counts.get()
            #print(hi)
            reordered.append(hi[1])

        return reordered

    def solvePuzzleSmart(self):
        self.count=0

        print("Unsolved Puzzle:")
        self.printGraph()
        self.makeQueue()

        start = self.squaresByConst.get()[1]
        if(self.solveSquareSmart(start)):
            print("Solution:")
            self.printGraph()
            #return self.graph
        else:
            print("No Solution.")
        print("Assignments made: " + str(self.count))

    def solveSquare(self, x, y, smartOrDumb):
        #if this is the last square, that means we've found a solution
        done = False #keeps track of whether constraints are violated
        nextSquare = self.getNext(x, y, smartOrDumb)
        nbors = self.findNeighbors(x, y)
        if self.graph[x][y].symbol != "_" and nextSquare is not None: #not a filled square and not the last square
            done = self.solveSquare(nextSquare[0], nextSquare[1], smartOrDumb)
        else: #this square must be blank
            for i in self.options: #loop through all possible colors, checking validity of each one
                self.graph[x][y].symbol = i #pick a color and assign it
                self.count += 1
                valid = self.checkConstraints(x, y, nbors) #make sure this doesn't violate any constraints
                if valid:
                    if nextSquare is None: #if this is the last square, then we've reached a solution, so return
                        return True
                    else:
                        done = self.solveSquare(nextSquare[0], nextSquare[1], smartOrDumb) #recursively call the solve method on the next square
                        if done == True: #end if we've reached a solution
                            return done
            if done == False: #rewrite over the symbol as blank of none of this options are valid
                self.graph[x][y].symbol = '_'
        return done #return solution or not

    def solveSquareSmart(self, current):
        #if this is the last square, that means we've found a solution

        done = False #keeps track of whether constraints are violated
        x = current.x
        y = current.y
        nbors = self.findNeighbors(x, y)

        #recurzive version
        if self.graph[x][y].symbol != "_": #not a filled square and not the last square
            print("hi")
            done = self.solveSquareSmart(self.squaresByConst.get()[1])
        else: #this square must be blank
            #reorganize the colors prioritizing most occuring in nbors
            self.options = self.countColors(nbors, self.options)
            for i in self.options: #loop through all possible colors, checking validity of each one
                self.graph[x][y].symbol = i
                self.count += 1
                #print(len(self.squaresByConst))
                #print("")
                #self.printGraph()
                #time.sleep(0.5)#pick a color and assign it
                valid = self.checkConstraints(x, y, nbors) #make sure this doesn't violate any constraints

                if valid:
                    blankNum = True
                    for i in range(self.xdim):
                        for j in range(self.ydim):
                            if self.graph[i][j].symbol == "_":
                                blankNum = False
                                break
                    if self.squaresByConst.empty(): #we've reached a solution, so return
                        return True
                    elif blankNum == True:
                        done = True
                        return done
                    else:
                        #update Constraints
                        self.makeQueue()

                        done = self.solveSquareSmart(self.squaresByConst.get()[1]) #recursively call the solve method on the next square

                        if done == True: #end if we've reached a solution
                            return done
            if done == False: #rewrite over the symbol as blank of none of this options are valid
                self.graph[x][y].symbol = '_'

        return done #return solution or not

    def findNeighbors(self, x, y): #returns all neighbors of a square in a list
        nbors = list(())
        if(x > 0):
            nbors.append(self.graph[x-1][y])
        if(y > 0):
            nbors.append(self.graph[x][y-1])
        if(x < self.xdim - 1):
            nbors.append(self.graph[x+1][y])
        if(y < self.ydim - 1):
            nbors.append(self.graph[x][y+1])
        return nbors

    def findMostConstrained(self):
        current = self.graph[0][0]
        for i in range(self.xdim):
            for j in range(self.ydim):
                self.graph[i][j].constrained = self.howConstrained(self.findNeighbors(i, j))
                if (self.graph[i][j].constrained >= current.constrained and self.graph[i][j].symbol == "_") or (current.symbol != "_" and self.graph[i][j].symbol == "_"):
                    current = self.graph[i][j]
        if current.symbol != "_":
            return None
        else:
            return [current.x, current.y]

    def howConstrained(self, square, nbors): #determines how constrained by finding number of non-blank neighbors
        count = 0
        for i in self.options:
            if self.checkConstraints(square.x, square.y, nbors):
                count += 1
        return len(self.options) - count

    def checkConstraints(self, x, y, nbors):
        i = self.graph[x][y].symbol #symbol of square we're testing
        valid = True #check that placing this value in this square doesn't violate any neighboring constraints
        nbors.append(self.graph[x][y])

        for j in nbors: #includes this square and all 4 of its neighbors
            if j.symbol == "_": #ignore blank spaces
                continue
            cnbors = self.findNeighbors(j.x, j.y)
            if j.symbol.isupper(): #Make sure endpoints don't have more than one matching color coming out of them and that if it doesn't have any, that it has at least one blank adjacent square
                symbolCount = includesSquare(j.symbol.lower(), cnbors)
                blankCount = includesSquare("_", cnbors)
                if symbolCount > 1: #more than one of same color connecting
                    valid = False
                if blankCount == 0 and symbolCount != 1: #no available ways to connect to endpoint
                    valid = False
            else: #Symbol is not an endpoint, but we have to make sure it's not blocked in by other colors either
                symbolCount = includesSquare(j.symbol, cnbors)
                symbolCount += includesSquare(j.symbol.upper(), cnbors)
                blankCount = includesSquare("_", cnbors)
                if symbolCount > 2: #too many of same color connecting
                    valid = False
                if symbolCount == 1 and blankCount < 1: #not enough blank spaces to connect
                    valid = False
                if symbolCount == 0 and blankCount < 2: #not enough blank spaces to connect
                    valid = False
        return valid

    def getNext(self, x, y, smartOrDumb): #returns next square, varying depending on whether we're using dumb or smart algorithm
        if smartOrDumb == "dumb":
            if x == self.xdim - 1 and y == self.ydim - 1:
                return None
            elif x == self.xdim - 1:
                return [0, y + 1]
            else:
                return [x + 1, y]
        elif smartOrDumb == "smart":
            if len(self.squaresByConst) == 0:
                return None
            else:
                square = self.squaresByConst.pop(0)
                return [square.x, square.y]
        else:
            #self.graph[x][y] = "1"
            nbors = self.findNeighbors(x, y)
            for i in nbors:
                #self.howConstrained(self.findNeighbors(i.x, i.y))
                i.constrained += 1
            answer = self.findMostConstrained()
            self.graph[x][y].symbol = "_"
            return answer

    def printGraph(self):
        for i in range(self.xdim):
            line = ""
            for j in range(self.ydim):
                line += self.graph[i][j].symbol
            print(line)

if __name__ == "__main__":
    print("hello world")
    file = str(sys.argv[1])

    with open(file) as f:
        lines = f.readlines()
    lines = [l.strip() for l in lines]

    dim = len(lines[0])
    dim2 = len(lines)
    graph = ""

    if dim != dim2:
        print("not a valid graph!")
    else:
        for l in lines:
            graph = graph + l

    gd = Graph(graph, dim, dim)
    print("Dumb CSP algorithm on graph {0}x{1}: ".format(str(dim), str(dim)))
    currentTime = time.time()
    gd.solvePuzzleDumb()
    print(time.time() - currentTime)

    gs = Graph(graph, dim, dim)
    print("Smart CSP algorithmon graph {0}x{1}: ".format(str(dim), str(dim)))
    currentTime = time.time()
    gs.solvePuzzleSmart()
    print(time.time() - currentTime)
