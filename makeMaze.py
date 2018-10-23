import random
from Grid import Grid
from graphics import color_rgb
import time
from Maze import Maze


def main():
    height= 101 # HEIGHT IS WIDTH
    width = 51 # WIDTH IS HEIGHT
    squareHeight = 10
    grid = Grid(squareHeight, width, height, name="Maze")
    randomisedDFS(grid, width, height)

def randomisedDFS(grid, width, height):
    
    maze = Maze(grid=grid)
    wait = 0.01

    background = color_rgb(0, 0, 0)
    pathcolor = color_rgb(255, 255, 255)
    activecolor = color_rgb(255, 0, 0)
    backtrackcolor = color_rgb(0, 0, 255)

    grid.fill(color=background) # make grid black

    maze.makeMaze(width,height)

    dx = [0, 1, 0, -1]; dy = [-1, 0, 1, 0] # 4 directions to move in the maze
    
    stack = [] # stores nodes with unvisited neighbors
    stack.append(maze.nodes[1][1]) # start at top left

#    intNode = stack[-2] # int, intermediate. Takes steps in twos, int is to fill inbetween.
    
    while len(stack) > 0:

        time.sleep(wait)

        # get new node from stack
        activeNode = stack[-1]
        activeNode.visited = True

        # find a new cell to add
        neighbors = [] # list of available neighbors
        for nextNode in maze.getNeighbors(activeNode):
            if not nextNode.visited: # check cell is unsolved
                neighbors.append(nextNode)

        # if 1 or more neighbors available then randomly select one and move
        if len(neighbors) > 0:
            activeNode.setColor(pathcolor)

            nextNode = neighbors[random.randint(0, len(neighbors) - 1)] # choose next node

            maze.connectNodes(activeNode, nextNode)

            maze.grid.drawLine(activeNode, nextNode, pathcolor)

            activeNode = nextNode

            stack.append(activeNode)
            activeNode.setColor(activecolor)

        # if no neighbors. getting nodes from stack
        else:
            
            popNode = stack.pop()
            if len(stack)>0:
                popNode.setColor(backtrackcolor)
                maze.grid.drawLine(popNode, stack[-1], backtrackcolor)
            else:
                popNode.setColor(backtrackcolor)
            

    grid.getMouse()
    grid.close()

def DFS():
    pass
    
if __name__ == "__main__":
    main()