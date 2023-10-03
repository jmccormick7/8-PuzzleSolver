## John McCormick 
## jcm258
## CSDS 391: Programming Assignment 1- Extra Credit
## Due: October 3rd, 2023 18:00:00

import random

class FifteenPuzzle():
    """
    A class representing a 15-puzzle
    """
    goalState0 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]   # The goal state of the puzzle with 0 as blank
    goalStateb = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 'b']]  # The goal state of the puzzle with b as blank



    def __init__(self, state = None):
        """
        Constructor for the FifteenPuzzle class
        args: state - (An optional parameter) a string representing the initial state of the puzzle Must be of the same format as setState takes ("x-x-x-x x-x-x-x x-x-x-x x-x-x-x")
        """
        if state != None:
            self.setState(state)
        else:
            self.setState("1-2-3-4 5-6-7-8 9-10-11-12 13-14-15-0")

    def setState(self, state):
        """
        Sets the state of the puzzle to the given state.
        args: state- a string representing the puzzle state (16 numbers in groups of 4, 0 or "b" for blank)
        returns: None
        """
        state = state.split(" ")
        self.state = []
        for nums in state:
            num = nums.split("-")
            row = []
            for i in range(0, 4):
                if num[i] == "b":
                    row.append("b")
                else:
                    row.append(int(num[i]))
            self.state.append(row)

    def getStateString(self) -> str:
        """
        Returns a string representing the current state of the puzzle
        args: None
        returns: a string representing the current state of the puzzle (in the xxx xxx xxx format)
        """
        string = ""
        for row in self.state:
            for num in row:
                string += str(num)
                string += "-"
            string = string[:-1]
            string += " "
        return string[:-1]

    def printState(self):
        """
        Prints the current state of the puzzle.
        args: None
        returns: None
        """
        for row in self.state:
            print(f"{row[0]} {row[1]} {row[2]} {row[3]}")

    def findBlank(self) -> tuple:
        """
        Method to find the blank square in the puzzle board
        args: None
        returns: tuple representing the location of the blank square
        """
        for row in range(0, 4):
            for col in range(0, 4):
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
        
    def validMoves(self) -> list:
        """ 
        Returns a list of valid directional moves for the blank square
        args: None
        returns: list of strings representing valid moves
        """
        blankCoords = self.findBlank()
        moves = []
        if blankCoords[0] != 0:
            moves.append("up")
        if blankCoords[0] != 3:
            moves.append("down")
        if blankCoords[1] != 0:
            moves.append("left")
        if blankCoords[1] != 3:
            moves.append("right")
        return moves
    
    def isGoal(self) -> bool:
        """
        Checks if the current state is the goal state
        args: None
        returns: True if the current state is the goal state, False otherwise
        """
        return self.state == FifteenPuzzle.goalState0 or self.state == FifteenPuzzle.goalStateb


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
            self.move(random.choice(self.validMoves()))

    def getHashString(self) -> str:
        """
        Returns a string representing the current state of the puzzle that is standardized to 0 as the blank square for hashing purposes
        args: None
        returns: a string representing the current state of the puzzle with 0 as the blank square
        """
        string = self.getStateString()
        string = string.replace("b", "0")
        return string

    def getHeuristic(self, hueristic: str) -> int:
        """
        Returns the value of a given state according to a heuristic function specified by the user for the 8-puzzle
        args: heuristic - a string representing the heuristic function to use (in this case h1 or h2)
        returns: a int representing the value of the state according to the heuristic function
        """
        if hueristic == "h1":
            return self.calculate_h1()
        else:
            return self.calculate_h2()

    def calculate_h1(self) -> int: 
        """
        Calculates the heuristic h1 value for a given state of the 8-puzzle (this calculates the current state)
        h1 is the number of misplaced tiles
        args: None
        returns: an int representing the heuristic value of the state
        """
        stateString = self.getStateString()
        stateString = stateString.replace(" ", "-")  #remove spaces, turn to dashes
        stateString = stateString.replace("b", "0") #replace b with 0 to standardize the heuristic calculation
        state = stateString.split("-")
        sum = 0
        for i in range(0,16):
            if state[i] != str(i + 1) and state[i] != "0":
                sum += 1
        return sum

        

    def calculate_h2(self) -> int: 
        """
        Calculates the heuristic h2 value for a given state of the 8-puzzle (this calculates the current state)
        h2 is the manhattan distance, or the sum of the distances of each tile from its goal position
        args: None
        returns: an int representing the heuristic value of the state
        """
        locations = {
            1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (0, 3),
            5: (1, 0), 6: (1, 1), 7: (1, 2), 8: (1, 3),
            9: (2, 0), 10: (2, 1), 11: (2, 2), 12: (2, 3),
            13: (3, 0), 14: (3, 1), 15: (3, 2), 0: (3, 3)
        }
        sum = 0
        for row in range(0, 4):
            for col in range(0, 4):
                if self.state[row][col] != 0 and self.state[row][col] != "b":
                    # This line adds onto the sum the manhattan distance of the current tile from its goal position
                    # The calculation is done by taking the row value and taking the absolute difference between it and the location goal state from the hash table
                    # Then, the same is done for the column value
                    sum += abs(row - locations[self.state[row][col]][0]) + abs(col - locations[self.state[row][col]][1])
                    print(sum)
        return sum
 
