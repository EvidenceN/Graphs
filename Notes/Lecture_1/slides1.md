# Slides https://docs.google.com/presentation/d/1RLYNJ6TWHaDE4MypgLjvG1lq7_f6kJTib7qV9JH70OU/edit#slide=id.g9270846f40_2_375

## Intro to Graphs

• A very versatile data structure that allows you to represent relationships between data
• Social network, flight schedule, word relationships, etc.


### COMPONENTS OF A GRAPH

• Vertex - also called nodes
• Edge - connects a pair of nodes
    • Unidirectional - Path from A to B doesn’t mean there’s a path from B to A
    • Bidirectional - A is friends with B, then B is friends with A
• Weight - used to represent a value associated with the edge (usually a cost)


### EXAMPLES OF GRAPHS

• Social Networks
    • Each node is a user, edges are friendships between nodes
    • Edges can also be to which groups you are a part of
• Transportation Systems (BART, Maps, etc.)
    • Each node is a location, each edge is a route to another one. A weight can represent time to get there
• The Internet!
    • Each page can be represented as a node, an directed edge is a link to another web page

## Graph Properties

• A graph can have multiple properties
• Knowing these different properties are important so you can build/solve graph problems!


### DIRECTED VS. UNDIRECTED

• A graph can be either directed or undirected
• Directed - An edge from A to B doesn’t mean there’s an edge from B to A
• Undirected - An edge from A to B means there’s also an edge from B to A

### CYCLIC VS. ACYCLIC

• Applies to directed graphs
• cyclic - there’s at least one path from a node back to itself
• acyclic - there are no paths such that no node can be traversed back to itself

### DENSE VS. SPARSE

• A graph can be sparse/dense or anything in between
• Dense - contains close to the maximum edges possible
• Sparse - contains close to the minimum edges possible

### WEIGHTED VS. UNWEIGHTED

• A graph can either be weighted or unweighted
• Weight determines a value associated with an edge (usually a cost)
• Weighted - Each edge has an associated value
• Unweighted - Each edge has no associated value

## Representing Graphs

### ADJACENCY LIST

• Use a dictionary with sets to represent the edges of a particular vertex to other neighboring vertices
• adjacencyList[i] is a list of all the edges to its neighbors for vertex i

### ADJACENCY LIST RUNTIME/SPACE COMPLEXITIES

• Space: O(vertices2)
    • Imagine a dense graph
• Add vertex: O(1)
• Remove vertex: O(vertices)
• Add edge: O(1)
• Remove edge: O(1)
• Find edge: O(1)
• Get all edges: O(1)

### ADJACENCY MATRIX

• Use a matrix to represent whether or not there exists an edge between two vertices
• matrix[i][j] is True if there exists an edge from vertex i to vertex j

### ADJACENCY MATRIX RUNTIME/SPACE COMPLEXITIES

• Space: O(vertices2)
    • Even in a sparse graph, but good for dense graphs b/c lists are space efficient
• Add vertex: O(vertices2)
• Remove vertex: O(vertices2)
• Add edge: O(1)
• Remove edge: O(1)
• Find edge: O(1)
• Get all edges: O(vertices)

### ADJACENCY MATRIX VS. ADJACENCY LISTS

• The best representation mainly depends on whether or not the graph is sparse/dense and what you’re optimizing for (space/runtime)
• Representing dense graphs are probably better with adjacency matrix because lists are very space efficient in comparison to dictionaries/sets
• You’ll probably deal with more adjacency lists

## Graph Traversals

• There are two primary ways to traverse a graph: Depth-first and Breadth-first
• Traversal vs. Search
    • In a search, you stop once you find the node you’re searching for
    • In a traversal, you traverse the entire graph

### DEPTH-FIRST TRAVERSAL

• Traverse the graph in a depth-ward motion using a stack/recursion

### DEPTH-FIRST TRAVERSAL ITERATIVE PSEUDOCODE

Picture in notebook

### DEPTH-FIRST TRAVERSAL RECURSIVE PSEUDOCODE

Picture in notebook

### BREADTH-FIRST

• Traverse the graph in a breadth-ward motion using a queue
• Very useful for finding shortest path from node to node

### BREADTH-FIRST SEARCH PSEUDOCODE

Picture in notebook

