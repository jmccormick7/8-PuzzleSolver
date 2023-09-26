## John McCormick 
## jcm258
## CSDS 391: Programming Assignment 1
## Due: September 26th, 2023 18:00:00

from EightPuzzle import EightPuzzle
from EightSearchNode import SearchNode
from search import GraphSearch
import pytest

#------------------------EightPuzzle.py Tests------------------------
"""
This file is used to test the basic functions of the EightPuzzle class 
using unit tests and pytest. This file is not proof of algorithmic 
effectiveness for the searches, it does however provide evidence for 
the class working in the intended way. This file proves the efficacy of 
the basic EightPuzzle class functions. It also proves the correctness 
of the heuristic functions that are used in the searches. 
"""

def test_init():
    # Test initialization with default goal state
    puzzle = EightPuzzle()
    assert puzzle.state == EightPuzzle.goalState0

    # Test initialization with custom state
    state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    stateSTR = "123 456 780"
    puzzle = EightPuzzle(stateSTR)
    assert puzzle.state == state

def test_setState():
    # Test setting state with valid state
    puzzle = EightPuzzle()
    state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    stateSTR = "123 456 780"
    puzzle.setState(stateSTR)
    assert puzzle.state == state

def test_move():
    # Test moving up
    puzzle = EightPuzzle("123 405 678")
    puzzle.move("up")
    assert puzzle.state == [[1, 0, 3], [4, 2, 5], [6, 7, 8]]

    # Test moving down
    puzzle = EightPuzzle("103 425 678")
    puzzle.move("down")
    assert puzzle.state == [[1, 2, 3], [4, 0, 5], [6, 7, 8]]

    # Test moving left
    puzzle = EightPuzzle("123 405 678")
    puzzle.move("left")
    assert puzzle.state == [[1, 2, 3], [0, 4, 5], [6, 7, 8]]

    # Test moving right
    puzzle = EightPuzzle("123 045 678")
    puzzle.move("right")
    assert puzzle.state == [[1, 2, 3], [4, 0, 5], [6, 7, 8]]

def test_getHashString():
    # Test getting hash string
    puzzle = EightPuzzle()
    # Test with default goal state
    assert puzzle.getHashString() == "012 345 678"
    # test that b turns to 0 every time
    puzzle.setState("b12 345 678")
    assert puzzle.getHashString() == "012 345 678"
    # test random case
    puzzle.setState("123 405 678")
    assert puzzle.getHashString() == "123 405 678"

#Test setting seed for randomizeState
def test_seed():
    puzzle = EightPuzzle()
    puzzle.randomizeState(25, 7)
    puzzle2 = EightPuzzle()
    puzzle2.randomizeState(25, 7)
    assert puzzle.state == puzzle2.state

def test_getStateString():
    # Test getting state string
    puzzle = EightPuzzle()
    assert puzzle.getStateString() == "012 345 678"

def test_h1Calculation():
    # Test h1 calculation
    # Hand calculated the heuristic value of the states for h1 and compared to actual result from code
    puzzle = EightPuzzle()
    assert puzzle.calculate_h1() == 0
    puzzle.setState("b12 345 678")
    assert puzzle.calculate_h1() == 0
    puzzle.setState("123 405 678")
    assert puzzle.calculate_h1() == 4
    puzzle.setState("876 534 210")
    assert puzzle.calculate_h1() == 8

def test_h2Calculation():
    # Test h2 calculation
    # Hand calculated the heuristic value of the states for h2 and compared to actual result from code
    puzzle = EightPuzzle()
    assert puzzle.calculate_h2() == 0
    puzzle.setState("b12 345 678")
    assert puzzle.calculate_h2() == 0
    puzzle.setState("123 405 678")
    assert puzzle.calculate_h2() == 6
    puzzle.setState("876 534 210")
    assert puzzle.calculate_h2() == 20

def test_isGoal():
    # Test isGoal
    puzzle = EightPuzzle()
    assert puzzle.isGoal() == True
    puzzle.setState("123 405 678")
    assert puzzle.isGoal() == False

def test_validMoves():
    # Test validMoves
    puzzle = EightPuzzle()
    assert puzzle.validMoves() == ["down", "right"]
    puzzle.setState("123 405 678")
    assert puzzle.validMoves() == ["up", "down", "left", "right"]
    puzzle.setState("103 425 678")
    assert puzzle.validMoves() == ["down", "left", "right"]
    puzzle.setState("123 045 678")
    assert puzzle.validMoves() == ["up", "down", "right"]

def test_Asearch_h1():
    # Test A* search using heuristic 1 this tests a basic case 
    puzzle = EightPuzzle()
    search = GraphSearch()
    # At this state the puzzle is already solved so the cost should be 0
    cost, path, nodes = search.solveAStar(puzzle, "h1")
    assert cost == 0
    assert path == []
    assert nodes == 1
    # actual solution was found using an online tool to solve the 8-puzzle my method then compares to the online solver
    puzzle.setState("123 405 678")
    cost, path, nodes = search.solveAStar(puzzle, "h1")
    assert cost == 14

def test_Asearch_h2():
    # Test A* search using heuristic 2 this tests a basic case
    puzzle = EightPuzzle()
    search = GraphSearch()
    # At this state the puzzle is already solved so the cost should be 0
    cost, path, nodes = search.solveAStar(puzzle, "h2")
    assert cost == 0
    assert path == []
    assert nodes == 1
    # actual solution was found using an online tool to solve the 8-puzzle my method then compares to the online solver
    puzzle.setState("123 405 678")
    cost, path, nodes = search.solveAStar(puzzle, "h2")
    assert cost == 14

def test_beamSearch():
    # Test the beam search using heuristic 2
    puzzle = EightPuzzle()
    search = GraphSearch()
    # At this state the puzzle is already solved so the cost should be 0
    cost, path, nodes = search.solveBeam(puzzle, 1)
    assert cost == 0
    assert path == []
    assert nodes == 1
    # actual solution was found using an online tool to solve the 8-puzzle my method then compares to the online solver
    #high kvalue to ensure that the solution is found
    puzzle.setState("312 658 074")
    cost, path, nodes = search.solveBeam(puzzle, 100)
    assert cost == 8
