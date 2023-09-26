## John McCormick 
## jcm258
## CSDS 391: Programming Assignment 1
## Due: September 26th, 2023 18:00:00

from EightPuzzle import EightPuzzle
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