## John McCormick 
## jcm258
## CSDS 391: Programming Assignment 1- Extra Credit
## Due: October 3rd, 2023 18:00:00

#------------------------FifteenPuzzle.py Tests------------------------
"""
This file is used to test the basic functions of the FifteenPuzzle class 
using unit tests and pytest. This file is not proof of algorithmic 
effectiveness for the searches, it does however provide evidence for 
the class working in the intended way. This file proves the efficacy of 
the basic FifteenPuzzle class functions. It also proves the correctness 
of the heuristic functions that are used in the searches. 
"""

from FifteenPuzzle import FifteenPuzzle
from search import GraphSearch

def test_init():
    # Test initialization with default goal state
    puzzle = FifteenPuzzle()
    assert puzzle.state == FifteenPuzzle.goalState0

    # Test initialization with custom state
    state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10 , 11, 12], [13, 0, 14, 15]]
    stateSTR = "1-2-3-4 5-6-7-8 9-10-11-12 13-0-14-15"
    puzzle = FifteenPuzzle(stateSTR)
    assert puzzle.state == state

def test_setState():
    # Test setting state with valid state
    puzzle = FifteenPuzzle()
    state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10 , 11, 12], [13, 0, 14, 15]]
    stateSTR = "1-2-3-4 5-6-7-8 9-10-11-12 13-0-14-15"
    puzzle.setState(stateSTR)
    assert puzzle.state == state

def test_getStateString():
    # Test getting state string
    puzzle = FifteenPuzzle()
    assert puzzle.getStateString() == "1-2-3-4 5-6-7-8 9-10-11-12 13-14-15-0"

#! edit from here 
def test_move():
    # Test moving up
    puzzle = FifteenPuzzle("1-2-3-4 5-6-7-8 9-0-11-12 13-10-14-15")
    puzzle.move("up")
    assert puzzle.state == [[1, 2, 3, 4], [5, 0, 7, 8], [9, 6, 11, 12], [13, 10, 14, 15]]

    # Test moving down
    puzzle.move("down")
    assert puzzle.state == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 11, 12], [13, 10, 14, 15]]

    # Test moving left
    puzzle.move("left")
    assert puzzle.state == [[1, 2, 3, 4], [5, 6, 7, 8], [0, 9, 11, 12], [13, 10, 14, 15]]

    # Test moving right
    puzzle.move("right")
    assert puzzle.state == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 11, 12], [13, 10, 14, 15]]

def test_getHashString():
    # Test getting hash string
    puzzle = FifteenPuzzle()
    # Test with default goal state
    assert puzzle.getHashString() == "1-2-3-4 5-6-7-8 9-10-11-12 13-14-15-0"
    # test that b turns to 0 every time
    puzzle.setState("1-2-3-4 5-6-7-8 9-10-11-12 13-14-15-b")
    assert puzzle.getHashString() == "1-2-3-4 5-6-7-8 9-10-11-12 13-14-15-0"
    # test random case
    puzzle.setState("1-2-3-4 5-6-7-8 9-10-11-12 14-13-15-0")
    assert puzzle.getHashString() == "1-2-3-4 5-6-7-8 9-10-11-12 14-13-15-0"

#Test setting seed for randomizeState
def test_seed():
    puzzle = FifteenPuzzle()
    puzzle.randomizeState(25, 7)
    puzzle2 = FifteenPuzzle()
    puzzle2.randomizeState(25, 7)
    assert puzzle.state == puzzle2.state

def test_h1Calculation():
    # Test h1 calculation
    # Hand calculated the heuristic value of the states for h1 and compared to actual result from code
    puzzle = FifteenPuzzle()
    assert puzzle.calculate_h1() == 0
    puzzle.setState("1-2-3-4 5-6-7-8 9-10-11-12 13-14-15-b")
    assert puzzle.calculate_h1() == 0
    puzzle.setState("1-3-5-7 2-4-6-8 9-10-11-12 0-13-15-14")
    assert puzzle.calculate_h1() == 8
    # puzzle.setState("876 534 210")
    # assert puzzle.calculate_h1() == 8

def test_h2Calculation():
    # Test h2 calculation
    # Hand calculated the heuristic value of the states for h2 and compared to actual result from code
    puzzle = FifteenPuzzle()
    assert puzzle.calculate_h2() == 0
    puzzle.setState("1-2-3-4 5-6-7-8 9-10-11-12 13-14-15-b")
    assert puzzle.calculate_h2() == 0
    puzzle.setState("1-3-5-7 2-4-6-8 9-10-11-12 0-13-15-14")
    assert puzzle.calculate_h2() == 15
    # puzzle.setState("876 534 210")
    # assert puzzle.calculate_h2() == 20

def test_isGoal():
    # Test isGoal
    puzzle = FifteenPuzzle()
    assert puzzle.isGoal() == True
    puzzle.setState("1-2-3-0 4-5-6-7 8-9-11-10 12-13-14-15")
    assert puzzle.isGoal() == False

def test_validMoves():
    # Test validMoves
    puzzle = FifteenPuzzle()
    assert puzzle.validMoves() == ["up", "left"]
    puzzle.setState("1-2-3-4 5-6-7-8 9-0-11-12 13-10-14-15")
    assert puzzle.validMoves() == ["up", "down", "left", "right"]
    puzzle.setState("0-2-3-4 5-6-7-8 9-1-11-12 13-10-14-15")
    assert puzzle.validMoves() == ["down", "right"]
    puzzle.setState("1-2-3-4 5-6-7-8 0-9-11-12 13-10-14-15")
    assert puzzle.validMoves() == ["up", "down", "right"]

def test_Asearch_h1():
    # Test A* search using heuristic 1 this tests a basic case 
    puzzle = FifteenPuzzle()
    search = GraphSearch()
    # At this state the puzzle is already solved so the cost should be 0
    cost, path, nodes = search.solveAStar(puzzle, "h1")
    assert cost == 0
    assert path == []
    assert nodes == 1
    # # actual solution was found using an online tool to solve the 8-puzzle my method then compares to the online solver
    # puzzle.setState("123 405 678")
    # cost, path, nodes = search.solveAStar(puzzle, "h1")
    # assert cost == 14

def test_Asearch_h2():
    # Test A* search using heuristic 2 this tests a basic case
    puzzle = FifteenPuzzle()
    search = GraphSearch()
    # At this state the puzzle is already solved so the cost should be 0
    cost, path, nodes = search.solveAStar(puzzle, "h2")
    assert cost == 0
    assert path == []
    assert nodes == 1
    # # actual solution was found using an online tool to solve the 8-puzzle my method then compares to the online solver
    # puzzle.setState("123 405 678")
    # cost, path, nodes = search.solveAStar(puzzle, "h2")
    # assert cost == 14

# def test_beamSearch():
#     # Test the beam search using heuristic 2
#     puzzle = EightPuzzle()
#     search = GraphSearch()
#     # At this state the puzzle is already solved so the cost should be 0
#     cost, path, nodes = search.solveBeam(puzzle, 1)
#     assert cost == 0
#     assert path == []
#     assert nodes == 1
#     # actual solution was found using an online tool to solve the 8-puzzle my method then compares to the online solver
#     #high kvalue to ensure that the solution is found
#     puzzle.setState("312 658 074")
#     cost, path, nodes = search.solveBeam(puzzle, 100)
#     assert cost == 8

