from graphics import *

class Grid:
    def __init__(self, squareHeight, width, height, name="test"):
    
        self.winWidth = width*squareHeight
        self.winHeight = height*squareHeight
        self.width = width
        self.height = height
        self.win = GraphWin(name, self.winHeight, self.winWidth)
        self.squareDim = squareHeight
        assert(round(height/self.squareDim)==height/self.squareDim, "noSquares must divide evenly into width and height")

    def getPointsForSquare(self, x, y):
        left = x*self.squareDim
        right = (x+1)*self.squareDim
        top = y*self.squareDim
        bottom = (y+1)*self.squareDim

        return Point(top, left), Point(bottom, right)

    def drawLine(self, node1, node2, color):
        diffx = (node2.x + node1.x)/2
        diffy = (node2.y + node1.y)/2

        if node2.x!=node1.x and node2.y==node1.y: # check that node2.x and node1.x !=
            self.toggleSquare(diffx, node1.y, color)

        elif node2.y!=node1.y and node2.x==node1.x:
            self.toggleSquare(node1.x, diffy, color)
        else: assert(False, "error in comparison")

    def hLine(self, x, y):
        left = x*self.squareDim
        right = (x+1)*self.squareDim
        h = y * self.squareDim

        return Point(h, left), Point(h, right)

    def vLine(self, x, y):
        top = y*self.squareDim
        bottom = (y+1)*self.squareDim
        h = x * self.squareDim
        return Point(top, h), Point(bottom, h)

    def toggleSquare(self, x, y, color):
        p1, p2 = self.getPointsForSquare(x, y)
        rect = Rectangle(p1, p2)

        rect.setFill(color)
        rect.setOutline(color)

        rect.draw(self.win)

    def fill(self, color=color_rgb(0, 0, 0)):
        rect = Rectangle(Point(0, 0), Point(self.winHeight, self.winWidth))
        rect.setFill(color)
        rect.setOutline(color)
        rect.draw(self.win)

    def getMouse(self):
        self.win.getMouse()

    def close(self):
        self.win.close()

    def showGrid(self):
        for i in range(10):
            for j in range(10):
                self.toggleSquare(i, j, True)
                time.sleep(0.1)
