# Graph Search Simulation

Breadth-First Search and Depth-First Search Traversal Simulation made in Python. 

Time Complexities of both Algorithms: `O(no.vertices + no.vertices)`

# Controls 
 - `1`: Views the Graph as a dictionary. The key is the vertex, and the value of the key is the list of the corresponding vertex's edges.
 - `2`: Simulates the Breadth-First Graph Search Algorithm.
 - `3`: Simulates the Depth-First Graph Search Algorithm.
 - `/quit`: Quits the simulation.


# Depth-First Search 

- Typically, a depth-first search uses a stack, however, instead of using another data structure, we just re-made the algorithm as a recursive algorithm.
- I also have integrated a print statement to view the process of the search. 
- To output different paths, for everytime the user types `y` to view another and the root vertex does have edges, the algorithm will pop the first edge of the list of edges as that is the initial edge the algorithm returned the path on, and will call the function again, but this time with a new list of edges where the initial edge is now not there anymore as it is already "visited". The algorithm will then run the search on the first edge of the new list of edges and will keep popping until the list is either empty of is there is no route to the desired vertex. However, if the user types `n` when prompted to see another path, the algorithm will NOT print another path.

# Breadth-First Search 
- Just like any other BFS algorithm, our version of the algorithm also uses a queue.
- Similar to Depth-First Search, I have integrated to a print statement to see the queue after every addition of a vertex to the stack during the search process.
- The BFS algorithm follows the same process as DFS to print another path. If the user types `y` when prompted, the algorithm will pop the first edge of the root vertex as that was the edge the algorithm first went on, and will recursively call the algorithm on itself on a new set of edges for the root vertex. This will keep running, until the user prompts `n`, or there is either no more edges, or there is no possible path to the target vertex. 


# More Information
- This is a simulation, hence, there is a base graph that the program runs based off of. The graph is located in `test_values.py`. Vertex values range from 1 to 6, hence, anything above that will result in the program denying the input.
- We could also re-construct each search, however, that would be unnecessary as it would be considered repetition of both the algorithm implementation and printing the actual process. 
- Made in Python



