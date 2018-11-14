from array import *
import time

"""script for for main"""
"""import CSP
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
        graph = graph + l"""


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
        self.squaresByConst = list(())
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

    def solvePuzzleDumb2(self):
        self.count=0
        print("Unsolved Puzzle:")
        self.printGraph()
        if self.solveSquareDumb2(0, 0):
            print("Solution:")
            self.printGraph()
            #return self.graph
        else:
            print("No solution.")
        print("Assignments made: " + str(self.count))

    def solvePuzzleSmart(self):
        self.count=0
        print("Unsolved Puzzle:")
        self.printGraph()
        for i in range(self.xdim):
            for j in range(self.ydim):
                if self.graph[i][j].symbol == "_":
                    self.graph[i][j].constrained = self.howConstrained(self.findNeighbors(i, j))
                    self.squaresByConst.append(self.graph[i][j])
        self.squaresByConst.sort(key=self.getConstrained, reverse=False)
        start = self.nextSquareSmart(0)
        if(self.solveSquareSmart(start[0], start[1], 0)):
            print("Solution:")
            self.printGraph()
            #return self.graph
        else:
            print("No Solution.")
        print("Assignments made: " + str(self.count))

        """print("Unsolved Puzzle:")
        self.printGraph()
        startSqr = self.findMostConstrained()
        if self.solveSquare(startSqr[0], startSqr[1], smartOrDumb="smart"):
            print("Solution:")
            self.printGraph()
            #return self.graph
        else:
            print("No solution.")"""
            
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

    def solveSquareSmart(self, x, y, index):
        #if this is the last square, that means we've found a solution
        done = False #keeps track of whether constraints are violated
        nextSquare = self.nextSquareSmart(index + 1)
        nbors = self.findNeighbors(x, y)
        if self.graph[x][y].symbol != "_" and nextSquare is not None: #not a filled square and not the last square
            done = self.solveSquareSmart(nextSquare[0], nextSquare[1], index + 1)
        else: #this square must be blank
            for i in self.options: #loop through all possible colors, checking validity of each one
                self.graph[x][y].symbol = i
                self.count += 1
                #print(len(self.squaresByConst))
                #self.printGraph()
                #time.sleep(0.5)#pick a color and assign it
                valid = self.checkConstraints(x, y, nbors) #make sure this doesn't violate any constraints
                if valid:
                    if nextSquare is None: #if this is the last square, then we've reached a solution, so return
                        return True
                    else:
                        done = self.solveSquareSmart(nextSquare[0], nextSquare[1], index + 1) #recursively call the solve method on the next square
                        if done == True: #end if we've reached a solution
                            return done
            if done == False: #rewrite over the symbol as blank of none of this options are valid
                self.graph[x][y].symbol = '_'
        return done #return solution or not

    def nextSquareSmart(self, index):
        if len(self.squaresByConst) - 1 < index:
            return None
        else:
            square = self.squaresByConst[index]
            return [square.x, square.y]

    def solveSquareDumb2(self, x, y):
        #if this is the last square, that means we've found a solution
        done = False #keeps track of whether constraints are violated
        nbors = self.findNeighbors(x, y)
        nextSquare = self.getNext(x, y, "dumb")
        if self.graph[x][y].symbol != "_" and nextSquare is not None: #not a filled square and not the last square
            done = self.solveSquareDumb2(nextSquare[0], nextSquare[1])
        else: #this square must be blank
            for i in self.options: #loop through all possible colors, checking validity of each one
                self.graph[x][y].symbol = i #pick a color and assign it
                #self.printGraph() #for debugging
                #time.sleep(1)
                if nextSquare is None:
                    done = True
                    for xi in range(self.xdim):
                        for yi in range(self.ydim):
                            if self.checkConstraints(xi, yi, nbors) == False:
                                done = False
                    if done == True:
                        return done
                else: 
                    done = self.solveSquareDumb2(nextSquare[0], nextSquare[1]) #recursively call the solve method on the next square
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
    
    def howConstrained(self, nbors): #determines how constrained by finding number of non-blank neighbors
        count = 0
        for i in nbors:
            if i.symbol == "_":
                count += 1
        return len(nbors) - count

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
        
g5x5 = Graph("B__RO___Y___Y___RO_G_BG__", 5, 5)
g7x7 = Graph("___O____B__GY____BR_____Y____________R____G___O__", 7, 7)
g8x8 = Graph("___R__G__BYP_______O_GR____P__________Y_____BOQ__Q______________", 8, 8)
g9x9 = Graph("D__BOK_____O__R_____RQ__Q__DB________G__________P____G__Y___Y________KP__________", 9, 9)
g10x10 = Graph("RG____________O___O__YP_Q___Q_____________G_____________R_________B___P__________Y______B___________", 10, 10)
g12x12 = Graph("_____________________________K_Y_G_____Y___G_____O_P______Q____R_OQ_________P_ARK____D__D_W_______________W___B_______B___________A_____________", 12, 12)
g14x14 = Graph("_______________B___A______________W____RP_D____A__W____________OB____G_OY______K_____________D____G___________________R_Y___________Q_______________________QP_______________K______________________", 14, 14)
currentTime = time.time()
#g5x5.solvePuzzleDumb2()
#g5x5.solvePuzzleSmart()
g7x7.solvePuzzleDumb()
print(time.time() - currentTime)

g5x5 = Graph("B__RO___Y___Y___RO_G_BG__", 5, 5)
g7x7 = Graph("___O____B__GY____BR_____Y____________R____G___O__", 7, 7)
g10x10 = Graph("RG____________O___O__YP_Q___Q_____________G_____________R_________B___P__________Y______B___________", 10, 10)
g8x8 = Graph("___R__G__BYP_______O_GR____P__________Y_____BOQ__Q______________", 8, 8)
g9x9 = Graph("D__BOK_____O__R_____RQ__Q__DB________G__________P____G__Y___Y________KP__________", 9, 9)
currentTime = time.time()
g7x7.solvePuzzleSmart()
#g5x5.solvePuzzleSmart()
print(time.time() - currentTime)