## John McCormick 
## jcm258
## CSDS 391: Programming Assignment 1
## Due: September 26th, 2023 18:00:00

import random

class EightPuzzle():
    """
    A class representing an 8-puzzle
    """
    goalState0 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]   # The goal state of the puzzle with 0 as blank
    goalStateb = [['b', 1, 2], [3, 4, 5], [6, 7, 8]]   # The goal state of the puzzle with b as blank


    def __init__(self, state = None):
        """
        Constructor for the EightPuzzle class
        args: state - (An optional parameter) a string representing the initial state of the puzzle Must be of the same format as setState takes ("xxx xxx xxx")
        returns: None
        """
        if state != None:
            self.setState(state)
        else:
            self.setState(self.goalState0)

    def setState(self, state):
        """
        Sets the state of the puzzle to the given state.
        args: state- a string representing the puzzle state (9 numbers in groups of 3, 0 for blank)
        returns: None
        """
        state = state.split()
        self.state = []
        for nums in state:
            row = []
            for i in range(0, 3):
                row.append(int(nums[i]))
            self.state.append(row)
    
    def printState(self):
        """
        Prints the current state of the puzzle.
        args: None
        returns: None
        """
        for row in self.state:
            print(f"{row[0]} {row[1]} {row[2]}")

    def findBlank(self) -> tuple:
        """
        Method to find the blank square in the puzzle board
        args: None
        returns: tuple representing the location of the blank square
        """
        for row in range(0, 3):
            for col in range(0, 3):
                if self.state[row][col] == 0 or self.state[row][col] == "b":
                    return (row, col)
  
    def move(self, direction: str):
        """ 
        Makes a move in the desired direction and updates the gameboard
        args: direction - a string representing the direction to move the blank square
        returns: None
        """
        blankCoords = self.findBlank()
        blank = self.state[blankCoords[0]][blankCoords[1]]
        if direction == "up":
            self.state[blankCoords[0]][blankCoords[1]] = self.state[blankCoords[0] - 1][blankCoords[1]]
            self.state[blankCoords[0] - 1][blankCoords[1]] = blank
        elif direction == "down":
            self.state[blankCoords[0]][blankCoords[1]] = self.state[blankCoords[0] + 1][blankCoords[1]]
            self.state[blankCoords[0] + 1][blankCoords[1]] = blank
        elif direction == "left":
            self.state[blankCoords[0]][blankCoords[1]] = self.state[blankCoords[0]][blankCoords[1] - 1]
            self.state[blankCoords[0]][blankCoords[1] - 1] = blank
        else:
            self.state[blankCoords[0]][blankCoords[1]] = self.state[blankCoords[0]][blankCoords[1] + 1]
            self.state[blankCoords[0]][blankCoords[1] + 1] = blank
        
    def randomizeState(self, n: int, seed: int = None):
        """ 
        Randomizes the state of the puzzle by making n random moves
        args: n - the number of random moves to make
                seed - (optional) a seed for the random number generator (for standardizing testing procedures)
        returns: None
        """
        if seed is not None:
            random.seed(seed)
        for i in range(0, n):
            self.move(random.choice(["up", "down", "left", "right"]))

    @classmethod
    def getHeuristic(cls, hueristic: str):
        """
        Returns the heuristic function specified by the user for the 8-puzzle
        args: heuristic - a string representing the heuristic function to use
        returns: a heuristic function
        """
        if hueristic == "h1":
            return cls.h1
        else:
            return cls.h2




if __name__ == "__main__":
    puzzle = EightPuzzle()
    puzzle.setState("123 456 780")
    puzzle.printState()