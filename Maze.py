import sys
from random import randint
import Grid


class Node:

    def __init__(self, x=None, y=None, grid=None, showProgess=True):
        self.grid = grid
        self.x = x
        self.y = y
        self.toNodes = []
        self.visited = False
        self.color = None
        self.showProgess = showProgess
        self.ref = "({},{})".format(self.x,self.y)
    
        
    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

    def setColor(self, color):
        assert(self.grid is not None, "No grid loaded to network")
        self.color = color
        self.grid.toggleSquare(self.x, self.y, color)

    def connect(self, node):
        self.toNodes.append(node)
        node.toNodes.append(self)



    def isVisited(self):
        return self.visited

class Maze(Node):
    def __init__(self, grid=None, showProgess=True):
        Node.__init__(self, grid=grid)
        
        self.prevx = None
        self.prevy = None
        self.nodes = []
        self.grid = grid
        self.activex = None
        self.activey = None
        self.showProgess = showProgess
    
    def __repr__(self):

        # print(Network()) does not work for very large networks
        out = ""
        out2 = ""
        for i in range(len(self.nodes)):
            for j, node in enumerate(self.nodes[i]):
                if len(node.toNodes)!=0: 
                    out += "{} --> ".format(self.nodes[i][j])
                    for toNode in self.nodes[i][j].toNodes:
                        out += "{}, ".format(toNode.ref)

                    out += "\n"
                # if len(self.nodes[i][j].toNodes)==0:
                #     out2 += "| {} |\n".format(self.nodes[i][j].ref)

        return out + " " + out2
   
    def writeRelations(self):
        # print(Network()) does not work for very large networks
        f = open("out.txt", "w")
        out = ""
        out2 = ""
        for i in range(len(self.nodes)):
            for j, node in enumerate(self.nodes[i]):
                if len(node.toNodes)!=0: 
                    out += "{} --> ".format(self.nodes[i][j])
                    for toNode in self.nodes[i][j].toNodes:
                        out += "{}, ".format(toNode.ref)

                    out += "\n"
                if len(self.nodes[i][j].toNodes)==0:
                    out2 += "{}\n".format(self.nodes[i][j].ref)
        f.write(out+" "+out2)

    def getNeighbors(self, node):
        dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0]
        out = []
        for i in range(4):

            nextx = node.x + 2 * dx[i]
            nexty = node.y + 2 * dy[i]
            if nextx >= 0 and nextx < self.grid.width and nexty >= 0 and nexty < self.grid.height: # cell is in grid range
                out.append(self.nodes[nexty][nextx])
        return out

    def makeMaze(self, width, height):
        self.nodes = [[self.createNode(x, y) for x in range(width)] for y in range(height)]  

    def createNode(self, x, y):
        """ creates a new node and adds it to the list of existing nodes
        """
        # create new node
        node = Node(x, y, grid=self.grid)
        # make ref its position in nodes
        # add node to network
        self.nodes.append(node)
        return node

    def connectNodes(self, node1, node2):
        """ connects existing node fromNode to toNode
        """
        # connect up Node
        node1.connect(node2)
        
    def deleteSingles(self):
        """ Need to rebuild for 2D list!
        """
        #assert(False, "REBUILD")

        for i in range(len(self.nodes)):
            for j, node in enumerate(self.nodes[i]):
                if len(node.toNodes)==0:
                    del(self.nodes[i][j])
                    print("DELETED: ", self.nodes[i][j])
    
    def size(self):
        return len(self.nodes)

    def exists(self, node):
        return node in self.nodes


    
