## Graphs 2

### DEPTH-FIRST VS BREADTH-FIRST

• Depth-first: Traverse in a depth-ward motion using a stack/recursion
• Breadth-first: Traverse in a breadth-ward motion using a queue

### NOTE ON GRAPH TRAVERSALS

• Sometimes, it doesn’t matter whether you do a depth-first or breadth-first search
• Breadth-first Search is very useful for finding the shortest path from a source to a destination

### DFS RECURSIVE

• There are two steps needed to implement a recursive solution: 
    • Base-case - when to return from your function
    • Recursive-case - when to recurse
• Base-cases:
    • When node is found, return the path you took
    • When no node is found return an empty path
• Recursive-case:
    • When you find a node that is not yet visited

## How to Solve Any Graph Problem

• Translate the problem into graph terminology
    • What are the vertices, edges, weights (if needed)?
• Build your graph
    • Do you even need to build a graph? Should you use an adjacency matrix/list?
• Traverse your graph
    • Should you use BFS/DFS? Do you need an auxiliary data structure?

### DESTINATION CITY

 Return the destination city
• Leetcode Link https://hackmd.io/@sIQnCbQ0T56A3KLAiNrlhQ/S1323O-Hv

### WORD LADDER

• Find the shortest transformation from beginWord to endWord, each transformation needs to be only 1 letter and needs to be in wordList

### TONIGHT’S PROJECT: EARLIEST ANCESTOR

• Find the earliest ancestor of a given individual
• https://github.com/LambdaSchool/Graphs/tree/master/projects/ancestor
