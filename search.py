## John McCormick 
## jcm258
## CSDS 391: Programming Assignment 1
## Due: September 26th, 2023 18:00:00

from EightPuzzle import EightPuzzle

class SearchNode():
    """
    Class for a search node that holds itself and its child nodes
    """

class GraphSearch():

    def maxNodes(self, nodes: int):
        """
        Sets a maximum number of nodes to be considered during a search
        args: nodes - the maximum number of nodes to be considered
        returns: None
        """
        self.maxNodes = nodes
    

    def solveAStar(self, puzzle: EightPuzzle, heuristicFunction: str) -> tuple:
        """
        Solves the given puzzle using A* search
        args: puzzle - the puzzle to be solved, heuristicFunction - a string representing the heuristic function to be used (an arg to the heuristic evaluation function)
        returns: a tuple with the number of moves needed, the path of moves, and the number of nodes expanded
        """
        pass

    def solveBeam(self, puzzle: EightPuzzle, k: int) -> tuple:
        """
        Solves the given puzzle using beam search
        args: puzzle - the puzzle to be solved, k - the number of nodes to be considered at each level
        returns: a tuple with the number of moves needed, the path of moves, and the number of nodes expanded
        """
        pass



