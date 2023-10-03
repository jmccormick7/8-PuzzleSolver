## John McCormick 
## jcm258
## CSDS 391: Programming Assignment 1
## Due: September 26th, 2023 18:00:00

from EightPuzzle import EightPuzzle
# Only change is to take a FifteenPuzzle rather than an EightPuzzle
from FifteenPuzzle import FifteenPuzzle

class SearchNode():
    """
    Class for a search node that holds itself and its child nodes
    """

    def __init__(self, parent = None, state: FifteenPuzzle = None, heuristicFunction: str = None, move = None):
        """
        Constructor for the SearchNode class
        args: parent - the parent node of the node, state - A puzzle object with the board position of the node
        returns: None
        """
        self.parent = parent
        self.state = state

        self.move = move

        self.heuristicValue = state.getHeuristic(heuristicFunction)
        if parent != None:
            self.cost = parent.cost + 1
        else:
            self.cost = 0
        
        self.totalCost = self.heuristicValue + self.cost

    def __eq__(self, other):
        """
        Checks if two nodes are equal (Overriding the default method for == so that the hash set works properly)
        args: other - the other node to compare to
        returns: True if the nodes are equal, False otherwise
        """
        if isinstance(other, SearchNode):
            return self.state.getHashString() == other.state.getHashString()
        else:
            return NotImplemented
    
    def __lt__(self, other):
        """
        Checks if one node is less than another, it uses total cost as the comparison
        Used for the priority queue as it defaults to comparing the objects in the case of cost ties
        args: other - the other node to compare to
        returns: True if the node is less than the other, False otherwise
        """
        if isinstance(other, SearchNode):
            return self.totalCost < other.totalCost
        else:
            return NotImplemented

    def __hash__(self):
        """
        Hashes the node (Overriding the default hash method so that the hash set works properly)
        args: None
        returns: the hash of the node
        """
        return hash(self.state.getHashString())

    def getMove(self) -> str:
        """
        Gets the move that was made to reach the current node
        args: None
        returns: a string representing the move that was made to reach the current node
        """
        return self.move

    def getPath(self) -> list:
        """
        Gets the path from the root node to the current node
        args: None
        returns: a list of the moves from the root node to the current node
        """
        path = []
        currentNode = self
        while currentNode.parent != None:
            path.append(currentNode.getMove())
            currentNode = currentNode.parent
        path.reverse()
        return path

    