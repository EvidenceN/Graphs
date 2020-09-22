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





