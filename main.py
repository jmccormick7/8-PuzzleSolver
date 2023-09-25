## John McCormick 
## jcm258
## CSDS 391: Programming Assignment 1
## Due: September 26th, 2023 18:00:00

from EightPuzzle import EightPuzzle
from search import GraphSearch


def main(args):
    """ 
    The main method from which the class will be run in the terminal
    args: args - the command line arguments
    returns: None
    """


def parseCommand(puzzle: EightPuzzle, command: list[str]):
    """
    Parses the command line arguments into actionable commands
    args: puzzle: the puzzle that the methods will be run on
            command - the command line arguments and parameters to parse
    returns: None
    """
    command = command.split()
    method = command[0]
    if method == "setState":
        parameters = "".join(command[1:])
        puzzle.setState(parameters)
    elif method == "printState":
        puzzle.printState()
    elif method == "move":
        puzzle.move(command[1])
    elif method == "randomizeState":
        puzzle.randomizeState()
    elif method == "solve":
        if command[1] == "A-star":
            pass
        elif command[1] == "beam":
            pass
    elif method == "maxNodes":
        pass
    else:
        print("Invalid command. Please try again.")




