# 8-PuzzleSolver

Code Design: 

The codebase is primarily split into 3 classes and 4 files:
EightPuzzle (EightPuzzle.py) class
This class contains all of the essential eight puzzle functions. 
Documentation for the entire class can be found at Appendix A.
This class holds the puzzle state, as well as processes the moves, the validity of moves, state changes, and heuristic evaluation
GraphSearch class (search.py)
This class contains the main search functionality 
Documentation for the entire class can be found at Appendix B
This class holds the methods for A* search and beam search, and does so independently, taking advantage of the modularity of the code, meaning with just a couple type changes it could be altered to process a different puzzle
SearchNode class (EightSearchNode.py)
This class contains the node class for all the graph searches.
Documentation for the entire class can be found at Appendix C
This class holds the functionality for getting the moves and getting the path of nodes. It stores the puzzle with the current state, as well as the parent node, and the move that was taken to get to this node. It also holds the current cost (the number of levels from the root node) and the heuristic value for the current state.
It also includes overrides of the __eq__ method, the __lt__ method, and the __hash__ method to enable better hashing for the A* method. 
main.py
This python script is the main way of interacting with the program through the command line. It contains the main functionality to read the file as a command line arg with the relative file path, as well as the functionality to parse commands from text, and print the move path.
All txt file testing of the program should be done with the following format:

The decision to split up the program into these 3 classes and 1 main script was to increase the modularity and the adaptability of the code base. The GraphSearch class can basically do graph search on any puzzle type with just a type change in the inputs for the puzzle, and a new node class that contains the new puzzle. So long as the new puzzle has the same functionality calls as EightPuzzle does, graph search should work on the new puzzle. This modularity helps make the search functions more useful in broader applications. It also allows for efficient distribution of work by allowing the puzzle to do all the puzzle moves and calculation, the search class to do all of the searching, and the node class to hold the data, and find its path.

A unique quirk to my code base is that because I do all the actions between 3 classes, and because my code works for both b and 0 as the blank square, using the priority queue required me to override the __eq__, __lt__ and __hash__ functions within my node class, and create a separate method to get a standardized “hash” string that I could use to rate equality between puzzles. 
The hash string method within EightPuzzle

Furthermore I chose to implement beam search using h2 as the heuristic function. This was because I wanted to prioritize getting closer to the goal state in terms of number of moves.I didn’t want the search to prioritize lessening misplaced tiles over lessening the overall number of moves away from the goal state the current state was.


Code Correctness:

To evaluate correctness I used two different methods. I tested using txt file input, and I used pytest unit tests to verify that key functionality was working within the individual classes. This unit testing helped me isolate where problems may or may not have been.

Note to grader: to use pytest, you must pip install pytest, and run the file with:
“pytest test.py”

All tests passed in the pytest. 

There were 2 tests for the txt files. The first test included many commands that tested the ability for the main.py to parse moves, printing commands, as well as handle both b and 0. It also randomized the state with a seed arg of 7. It then did various methods of solving the puzzle. 

The second test included examples unsolvable to test that failed tests would not crash and would output that the test indeed failed. 

Experiments:
Data Collected from running 10 terminal instances in which for every variation below 100 random trials were conducted and then these 10 instances had their data aggregated into the tables below:

<img width="605" alt="Screenshot 2023-09-28 at 2 27 53 PM" src="https://github.com/jmccormick7/8-PuzzleSolver/assets/123213439/a7a9f70e-10b1-4bbb-9cca-7fb8365e068f">


How does the fraction of solvable puzzles from random initial states vary with the maxNodes limit? 

For all the three methods, in general, as maxNodes increases as does the share of puzzles that can be solved. However this does seem to at times have a lesser effect with the beam search, as the k value seems to be a larger constraint. But for both heuristics in A* search, there was an increase in the percentage of puzzles solved as maxNodes increased. This makes sense as the longer A* is allowed to search for the more solutions it will find. This is seen with the increase in average moves per solution as the A* algorithm is able to dig deeper. Essentially maxNodes increasing increases the depth to which A* can search and longer solutions are then unlocked. However with beam search the opposite seems to be true. While yes as maxNodes increases so too does the percentage of puzzles solved, as k values increase average move number decreases along with the increase in problems solved. This suggests that k value is more important to the search algorithm as it is able to search down more branches thus having a better chance of finding the shortest path. So maxNodes helps beam search solve more, but ultimately the larger impact is on the efficacy of the k value for beam search.

For A* search, which heuristic is better?

The Manhattan distance heuristic (or h2) is better. This is seen as the average time per search is significantly less at higher maxNode values. But at the same maxNode values, bar the maximum and 1, h2 solves a larger proportion of the puzzles than h1 does, suggesting that the Manhattan distance heuristic is a better performing heuristic function for A* search. 

How does the solution length vary across the three search methods

For A* Search there is an increase in average solution length associated with an increase in maxNode value. This makes sense as A* getting access to more nodes allows A* to search deeper and find longer paths. However for beam search while that trend does exist, a much more significant trend is an increase in k leading to an overall decrease in average solution length. This too makes sense, as since beam search is based on BFS, increasing the number of nodes to evaluate at any given level increases the odds that the shortest path is found. That is because sometimes the shortest path includes short term negative heuristic gain to set up larger gains in later moves. Beam search cannot consider these as it will only expand the top k moves in terms of short term gain. Unlike A* which will expand the lowest total cost, so it will come back to ideal paths eventually.

For each of the three search methods, what fraction of your generated problems were solvable. 

For A* Search using h1, the average percent of problems that were solvable was 27%. For A* Search using h2, the average percent of problems that were solvable was 44.7%. For beam search with k = 1, it was 15.2%, for k -5 it was 26.5%, for k = 10 it was 31.5%, and for k=100 it was 33.7%. Based on these results it can be collected that A* search with h2 as a heuristic was the best performing search method. Especially considering that unbounded searches took an average time of .13 seconds to complete while solving 100% of puzzles it makes sense that this solution would be best. Although 100,000 maxNodes beam search with k = 100 yielded similar results faster, although with longer average paths. 

Discussion:

Based on my experiments I would say that A* search using h2 was the most optimal considering the smaller average solution length. However beam search using 100 as k and 100,000 as maxNodes, performed faster. Because of this I would probably be inclined to use beam search with 100 as k if I had spatial constraints. This is because the algorithm only saves 100 nodes at a time, compared to A* which holds all visited nodes and unexplored nodes. All the nodes do store history, so this isn’t a differentiator between the two. But it does seem that A* always found the optimal solution when unbounded and using h2 as a heuristic.

I had difficulty implementing beam search especially without the visited hash set that A* has. I was for a long time not preventing infinite loops from forming, and it took me some time to figure out exactly how I should have done it. Furthermore testing was difficult because of the temporal and computational complexity. I ran 10 simultaneous tests of all methods, and it took 18 minutes each on 98% CPU usage just to do 100 iterations of each method and parameters. This major resource used in getting the metrics used to do the analysis was difficult to work with at times. 
