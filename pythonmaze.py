from array import *

def includesSquare(symbol, symbolList):
    count = 0
    while symbol in symbolList:
        symbolList.remove(symbol)
        count += 1
    return count

class Square:
    def __init__(self, symbol):
        self.symbol = symbol

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
                    line.append(Square(inString[k]))
                    if inString[k] not in self.colors:
                        self.colors.add(inString[k])
                    k += 1
            self.graph.append(line)
        self.colors.remove("_")
    def getOptions(self, x, y):
        options = set(())
        for i in self.colors:
            options.add(i.lower())
        usedSymbols = []
        if x > 0:
            l = self.graph[x-1][y].symbol
            usedSymbols.append(l)
        if x < self.xdim - 2:
            r = self.graph[x+1][y].symbol
            usedSymbols.append(r)
        if y < self.ydim - 2:
            u = self.graph[x][y+1].symbol
            usedSymbols.append(u)
        if y > 0:
            d = self.graph[x][y-1].symbol
            usedSymbols.append(d)
        if x > 0 and y > 0:
            dl = self.graph[x-1][y-1].symbol
            usedSymbols.append(dl)
        if x > 0 and y < self.ydim - 2:
            ul = self.graph[x-1][y+1]
            usedSymbols.append(ul)
        if x < self.xdim - 2 and y > 0:
            dr = self.graph[x+1][y-1].symbol
            usedSymbols.append(dr)
        if x < self.xdim - 2 and y < self.ydim - 2:
            ur = self.graph[x+1][y+1].symbol
            usedSymbols.append(ur)
            
        while "_" in usedSymbols:
            usedSymbols.remove("_")
        for i in usedSymbols:
            usedSymbols.pop(usedSymbols.index(i))
            if i in usedSymbols:
                usedSymbols.pop(usedSymbols.index(i))
                if i in usedSymbols:
                    options.remove(i)
                    
        for i in options:
            print(i)
        print(self.graph[x][y].symbol)
    
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
g5x5.getOptions(3, 3)
g7x7.printGraph()
g7x7.getOptions(4, 4)
g14x14.printGraph()
g14x14.getOptions(7, 7)