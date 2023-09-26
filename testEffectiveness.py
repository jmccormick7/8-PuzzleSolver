## John McCormick 
## jcm258
## CSDS 391: Programming Assignment 1
## Due: September 26th, 2023 18:00:00

from itertools import permutations
from EightPuzzle import EightPuzzle
from EightSearchNode import SearchNode
from search import GraphSearch
import random
import time

def is_solvable(state):
    """
    Checks if a given state of the 8-puzzle is solvable. This uses the fact that a state is solvable if the number of inversions is even.
    Args: state (tuple): A permutation of the set {0, 1, 2, 3, 4, 5, 6, 7, 8}  
    Returns: bool: True if the state is solvable, False otherwise.
    """
    # Calculate the number of inversions in the state
    inversions = 0
    for i in range(9):
        for j in range(i + 1, 9):
            if state[j] and state[i] and state[i] > state[j]:
                inversions += 1
                
    # A state is solvable if the number of inversions is even
    return inversions % 2 == 0
start_time = time.time()
# Generate all possible states
all_states = permutations(range(9))

# Filter out the unsolvable states
solvable_states = [state for state in all_states if is_solvable(state)]
solvable_states = [' '.join([''.join(map(str, state[i:i+3])) for i in range(0, 9, 3)]) for state in solvable_states]
numStates = len(solvable_states)

end_time = time.time()
runtime = end_time - start_time
print(runtime)

#test A* search maxNodes of 1 (h1 heuristic)
start_time = time.time()
search = GraphSearch()
numSuccess = 0
numMoves = 0
puzzle = EightPuzzle()
search.setMaxNodes(1)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveAStar(puzzle, "h1")
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("A* search with maxNodes of 1 (h1)")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test A* search maxNodes of 10 (h1 heuristic)
start_time = time.time()

numStates = len(solvable_states)
numSuccess = 0
numMoves = 0
search.setMaxNodes(10)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveAStar(puzzle, "h1")
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("A* search with maxNodes of 10 (h1)")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test A* search maxNodes of 100 (h1 heuristic)
start_time = time.time()
numSuccess = 0
numMoves = 0
search.setMaxNodes(100)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveAStar(puzzle, "h1")
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("A* search with maxNodes of 100 (h1)")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test A* search maxNodes of 1000 (h1 heuristic)
start_time = time.time()
numMoves = 0
numStates = len(solvable_states)
numSuccess = 0
search.setMaxNodes(1000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveAStar(puzzle, "h1")
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("A* search with maxNodes of 1000 (h1)")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

start_time = time.time()

numStates = len(solvable_states)
#test A* search maxNodes of 10,000 (h1 heuristic)
numSuccess = 0
numMoves = 0
search.setMaxNodes(10000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveAStar(puzzle, "h1")
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("A* search with maxNodes of 10,000 (h1)")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves)) 
print("\n")

end_time = time.time()
print(end_time - start_time)

start_time = time.time()

#test A* search maxNodes of 2**63 - 1 (max int) (h1 heuristic)
numSuccess = 0
numMoves = 0
search.setMaxNodes(2**63 - 1)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveAStar(puzzle, "h1")
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("A* search with maxNodes of 2**63 - 1 (h1)")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)


#test A* search maxNodes of 1 (h2 heuristic)
start_time = time.time()
numSuccess = 0
numMoves = 0
search.setMaxNodes(1)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveAStar(puzzle, "h2")
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("A* search with maxNodes of 1 (h2)")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test A* search maxNodes of 10 (h2 heuristic)
start_time = time.time()

numStates = len(solvable_states)
numSuccess = 0
numMoves = 0
search.setMaxNodes(10)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveAStar(puzzle, "h2")
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("A* search with maxNodes of 10 (h2)")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test A* search maxNodes of 100 (h2 heuristic)
start_time = time.time()
numSuccess = 0
numMoves = 0
search.setMaxNodes(100)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveAStar(puzzle, "h2")
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("A* search with maxNodes of 100 (h2)")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test A* search maxNodes of 1000 (h2 heuristic)
start_time = time.time()

numStates = len(solvable_states)
numSuccess = 0
numMoves = 0
search.setMaxNodes(1000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveAStar(puzzle, "h2")
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("A* search with maxNodes of 1000 (h2)")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

start_time = time.time()

numStates = len(solvable_states)
#test A* search maxNodes of 10,000 (h2 heuristic)
numSuccess = 0
numMoves = 0
search.setMaxNodes(10000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveAStar(puzzle, "h2")
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("A* search with maxNodes of 10,000 (h2)")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

start_time = time.time()

#test A* search maxNodes of 2**63 - 1 (max int) (h2 heuristic)
numSuccess = 0
numMoves = 0
search.setMaxNodes(2**63 - 1)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveAStar(puzzle, "h2")
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("A* search with maxNodes of 2**63 - 1 (h2)")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)



#test beam search maxNodes of 1 (k = 1)
start_time = time.time()
numSuccess = 0
numMoves = 0
search.setMaxNodes(1)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 1)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 1 and k = 1")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test beam search maxNodes of 10 (k = 1)
start_time = time.time()

numStates = len(solvable_states)
numSuccess = 0
numMoves = 0
search.setMaxNodes(10)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 1)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 10 and k = 1")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test beam search maxNodes of 100 (k = 1)
start_time = time.time()
numSuccess = 0
numMoves = 0
search.setMaxNodes(100)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 1)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 100 and k = 1")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test beam search maxNodes of 1000 (k = 1)
start_time = time.time()

numStates = len(solvable_states)
numSuccess = 0
numMoves = 0
search.setMaxNodes(1000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 1)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 1000 and k = 1")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

start_time = time.time()

numStates = len(solvable_states)
#test beam search maxNodes of 10,000 (k = 1)
numSuccess = 0
numMoves = 0
search.setMaxNodes(10000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 1)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 10,000 and k = 1")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

start_time = time.time()

#test beam search maxNodes of 100000 (k = 1)
numSuccess = 0
numMoves = 0
search.setMaxNodes(100000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 1)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 100000 and k = 1")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test beam search maxNodes of 1 (k = 5)
start_time = time.time()
numSuccess = 0
numMoves = 0
search.setMaxNodes(1)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 5)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 1 and k = 5")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test beam search maxNodes of 10 (k = 5)
start_time = time.time()

numStates = len(solvable_states)
numSuccess = 0
numMoves = 0
search.setMaxNodes(10)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 5)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 10 and k = 5")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test beam search maxNodes of 100 (k = 5)
start_time = time.time()
numSuccess = 0
numMoves = 0
search.setMaxNodes(100)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 5)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 100 and k = 5")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test beam search maxNodes of 1000 (k = 5)
start_time = time.time()

numStates = len(solvable_states)
numSuccess = 0
numMoves = 0
search.setMaxNodes(1000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 5)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 1000 and k = 5")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

start_time = time.time()

numStates = len(solvable_states)
#test beam search maxNodes of 10,000 (k = 5)
numSuccess = 0
numMoves = 0
search.setMaxNodes(10000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 5)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 10,000 and k = 5")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

start_time = time.time()

#test beam search maxNodes of 100000 (k = 5)
numSuccess = 0
numMoves = 0
search.setMaxNodes(100000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 5)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 100000 and k = 5")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test beam search maxNodes of 1 (k = 10)
start_time = time.time()
numSuccess = 0
numMoves = 0
search.setMaxNodes(1)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 10)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 1 and k = 10")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test beam search maxNodes of 10 (k = 10)
start_time = time.time()

numStates = len(solvable_states)
numSuccess = 0
numMoves = 0
search.setMaxNodes(10)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 10)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 10 and k = 10")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test beam search maxNodes of 100 (k = 10)
start_time = time.time()
numSuccess = 0
numMoves = 0
search.setMaxNodes(100)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 10)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 100 and k = 10")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test beam search maxNodes of 1000 (k = 10)
start_time = time.time()

numStates = len(solvable_states)
numSuccess = 0
numMoves = 0
search.setMaxNodes(1000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 10)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 1000 and k = 10")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

start_time = time.time()

numStates = len(solvable_states)
#test beam search maxNodes of 10,000 (k = 10)
numSuccess = 0
numMoves = 0
search.setMaxNodes(10000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 10)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 10,000 and k = 10")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

start_time = time.time()

#test beam search maxNodes of 100000 (k = 10)
numSuccess = 0
numMoves = 0
search.setMaxNodes(100000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 10)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 100000 and k = 10")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)


#test beam search maxNodes of 1 (k = 100)
start_time = time.time()
numSuccess = 0
numMoves = 0
search.setMaxNodes(1)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 100)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 1 and k = 100")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test beam search maxNodes of 10 (k = 100)
start_time = time.time()

numStates = len(solvable_states)
numSuccess = 0
numMoves = 0
search.setMaxNodes(10)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 100)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 10 and k = 100")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test beam search maxNodes of 100 (k = 100)
start_time = time.time()
numSuccess = 0
numMoves = 0
search.setMaxNodes(100)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 100)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 100 and k = 100")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

#test beam search maxNodes of 1000 (k = 100)
start_time = time.time()

numStates = len(solvable_states)
numSuccess = 0
numMoves = 0
search.setMaxNodes(1000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 100)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 1000 and k = 100")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

start_time = time.time()

numStates = len(solvable_states)
#test beam search maxNodes of 10,000 (k = 100)
numSuccess = 0
search.setMaxNodes(10000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 100)
    if cost != None:
        numSuccess += 1
print("Beam search with maxNodes of 10,000 and k = 100")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)

start_time = time.time()

#test beam search maxNodes of 100000 (k = 100)
numSuccess = 0
numMoves = 0
search.setMaxNodes(100000)
for i in range(0, 100):
    state = solvable_states[random.randint(0, numStates - 1)]
    puzzle.setState(state)
    cost, path, nodes = search.solveBeam(puzzle, 100)
    if cost != None:
        numSuccess += 1
        numMoves += cost
print("Beam search with maxNodes of 100,000 and k = 100")
print("Number of successes: " + str(numSuccess))
print("Number of failures: " + str(100 - numSuccess))
print("Success rate: " + str(numSuccess / 100))
print("Total number of moves for successes: " + str(numMoves))
print("\n")

end_time = time.time()
print(end_time - start_time)