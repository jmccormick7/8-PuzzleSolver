## John McCormick 
## jcm258
## CSDS 391: Programming Assignment 1 - Extra Credit
## Due: October 3rd, 2023 18:00:00

import time
from itertools import permutations
from search import GraphSearch
from FifteenPuzzle import FifteenPuzzle
import random 


def is_solvable(state):
    """
    Checks if a given state of the 8-puzzle is solvable. This uses the fact that a state is solvable if the number of inversions is even.
    Args: state (tuple): A permutation of the set {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}  
    Returns: bool: True if the state is solvable, False otherwise.
    """
    # Calculate the number of inversions in the state
    inversions = 0
    for i in range(16):
        for j in range(i + 1, 16):
            if state[j] and state[i] and state[i] > state[j]:
                inversions += 1
                
    # A state is solvable if the number of inversions is even
    return inversions % 2 == 0
#! The permutations of 16 are just too large to realistically compute so I will use random move generation from a solvable state
# start_time = time.time()
# # Generate all possible states
# all_states = permutations(range(16))

# # Filter out the unsolvable states
# solvable_states = [state for state in all_states if is_solvable(state)]
# solvable_states = [' '.join([''.join(map(str, state[i:i+3])) for i in range(0, 9, 3)]) for state in solvable_states]
# numStates = len(solvable_states)

# end_time = time.time()
# runtime = end_time - start_time
# print(runtime)


search = GraphSearch()
puzzle = FifteenPuzzle()
start_time = time.time()

#test A* search maxNodes of 10,000 (h1 heuristic)
numSuccess = 0
numMoves = 0
search.setMaxNodes(10000)
for i in range(0, 100):
    puzzle.setState("1-2-3-4 5-6-7-8 9-10-11-12 13-14-15-0")
    puzzle.randomizeState(50, 711)
    cost, path, nodes = search.solveAStar(puzzle, "h1")
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("A* search with maxNodes of 10,000 (h1)")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves)) 


end_time = time.time()
runtime = end_time - start_time
print(runtime)
print("\n")
start_time = time.time()
#test A* search maxNodes of 10,000 (h2 heuristic)
numSuccess = 0
numMoves = 0
search.setMaxNodes(10000)
for i in range(50, 100):
    puzzle.setState("1-2-3-4 5-6-7-8 9-10-11-12 13-14-15-0")
    puzzle.randomizeState(50, 711)
    cost, path, nodes = search.solveAStar(puzzle, "h2")
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("A* search with maxNodes of 10,000 (h2)")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))


end_time = time.time()
runtime = end_time - start_time 
print(runtime)
print("\n")