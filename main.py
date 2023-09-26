## John McCormick 
## jcm258
## CSDS 391: Programming Assignment 1
## Due: September 26th, 2023 18:00:00

from EightPuzzle import EightPuzzle
from search import GraphSearch
import sys


def main():
    """ 
    The main method from which the class will be run in the terminal
    args: args - the command line arguments
    returns: None
    """
    puzzle = EightPuzzle()
    search = GraphSearch()
    if len(sys.argv) < 2:
        print("Please provide txt file to read commands from")
        return
    
    filename = sys.argv[1]

    try:
        file = open(filename, "r")
        for line in file:
            parseCommand(puzzle, search, line)
            
    except FileNotFoundError:
        print("File not found. Please try again.")
        return


def parseCommand(puzzle: EightPuzzle, search: GraphSearch, command: str):
    """
    Parses the command line arguments into actionable commands
    args: puzzle: the puzzle that the methods will be run on
            command - the command line arguments and parameters to parse
    returns: None
    """
    command = command.replace("\n", "") #remove the newline character
    command = command.split(" ")
    method = command[0]
    if method == "setState":
        parameters = " ".join(command[1:])
        puzzle.setState(parameters)
    elif method == "printState":
        puzzle.printState()
        print("\n")
    elif method == "move":
        puzzle.move(command[1])
    elif method == "randomizeState":
        if len(command) == 2:
            puzzle.randomizeState(int(command[1]))
        else:
            puzzle.randomizeState(int(command[1]), int(command[2]))
    elif method == "solve":
        if command[1] == "A-star":
            cost, path, nodes = search.solveAStar(puzzle, command[2])
        elif command[1] == "beam":
            cost, path, nodes = search.solveBeam(puzzle, int(command[2]))
        if cost == None:
            print("No solution found.")
            print("Nodes expanded: " + str(nodes))
        else:
            print("Moves: " + str(cost))
            print("Nodes expanded: " + str(nodes))
            print_path(path)
    elif method == "maxNodes":
        search.setMaxNodes(int(command[1]))
    else:
        print("Invalid command. Please try again.")

def print_path(path: list):
    """
    Prints the path of moves
    args: path - the path to be printed
    returns: None
    """
    string = ""
    for move in path:
        string += str(move) + ", "
    print(string[:-2])

if __name__ == "__main__":
    main()



