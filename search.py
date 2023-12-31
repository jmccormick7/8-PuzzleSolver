## John McCormick 
## jcm258
## CSDS 391: Programming Assignment 1
## Due: September 26th, 2023 18:00:00

from EightPuzzle import EightPuzzle
#! only change in this file to to take Fifteen Puzzles rather than 8 puzzles
from FifteenPuzzle import FifteenPuzzle
from EightSearchNode import SearchNode
import heapq # For priority queue (allows usage of heapq.heappush and heapq.heappop)



class GraphSearch():
    """
    This class holds all of the graph searches for any puzzles given certain methods within the puzzle class itself.
    """

    def __init__(self):
        """
        Constructor for the GraphSearch class
        args: None
        returns: None
        """
        self.maxNodes = 10000 #arbitrary max nodes value set to 10000


    def setMaxNodes(self, nodes: int):
        """
        Sets a maximum number of nodes to be considered during a search
        args: nodes - the maximum number of nodes to be considered
        returns: None
        """
        self.maxNodes = nodes
    

    def solveAStar(self, puzzle: FifteenPuzzle, heuristicFunction: str) -> tuple:
        """
        Solves the given puzzle using A* search
        args: puzzle - the puzzle to be solved, heuristicFunction - a string representing the heuristic function to be used (an arg to the heuristic evaluation function)
        returns: a tuple with the number of moves needed, the path of moves, and the number of nodes expanded
        """
        frontier = [] # unexplored nodes that need to be expaned (priority queue)
        explored = set() # the explored nodes that have been expanded (hash set)

        nodesGenerated = 1 # the number of nodes generated (including the first node)
        nodesExplored = 0

        # Create the first node (root node)
        root = SearchNode(None, puzzle, heuristicFunction)
        heapq.heappush(frontier, (root.totalCost, root))

        while len(frontier) > 0:

            if nodesExplored > self.maxNodes:
                return (None, [], nodesGenerated)

            #use the node with the lowest total cost:
            currentNode = frontier[0][1]
            if currentNode not in explored:
                explored.add(heapq.heappop(frontier)[1])
                nodesExplored += 1
            else:
                heapq.heappop(frontier)
                continue

            #Check for the goal state
            if currentNode.state.isGoal():
                return (currentNode.cost, currentNode.getPath(), len(explored))
            
            #create children
            for move in currentNode.state.validMoves():
                string = currentNode.state.getStateString()
                childPuzzle = FifteenPuzzle(string)
                childPuzzle.move(move)
                child = SearchNode(currentNode, childPuzzle, heuristicFunction, move)
                if child.state.isGoal():
                    return (child.cost, child.getPath(), nodesGenerated)
                if child not in explored:
                    heapq.heappush(frontier, (child.totalCost, child))
                    nodesGenerated += 1



    def solveBeam(self, puzzle: FifteenPuzzle, k: int) -> tuple:
        """
        Solves the given puzzle using beam search
        args: puzzle - the puzzle to be solved, k - the number of nodes to be considered at each level
        returns: a tuple with the number of moves needed, the path of moves, and the number of nodes expanded
        """
        root = SearchNode(None, puzzle, "h2")
        frontier = [root]
        explored = set() # the explored nodes that have been expanded (hash set)
        nodesGenerated = 1
        
        while frontier:
            next = []
            for node in frontier:
                if node.state.isGoal():
                    return (node.cost, node.getPath(), nodesGenerated)
                for move in node.state.validMoves():
                    string = node.state.getStateString()
                    childPuzzle = FifteenPuzzle(string)
                    childPuzzle.move(move)
                    child = SearchNode(node, childPuzzle, "h2", move)
                    if child == node.parent:
                        continue
                    nodesGenerated += 1
                    if child.state.isGoal():
                        return (child.cost, child.getPath(), nodesGenerated)
                    next.append(child)
            if next == []:
                return (None, [], nodesGenerated)
            frontier = sorted(next, key=lambda x: x.totalCost)[:k]
            if nodesGenerated > self.maxNodes:
                break
        
        return (None, [], nodesGenerated)



