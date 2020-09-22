# Graph Traversals

from collections import deque

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id] if vertex_id in self.vertices else set()

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        visited = set()
        queue = deque()
        queue.append(starting_vertex)
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.vertices[currNode]:
                    queue.append(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set()
        stack = deque()
        stack.append(starting_vertex)
        while len(stack) > 0:
            currNode = stack.pop()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.vertices[currNode]:
                    stack.append(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        self.dft_recursive_helper(starting_vertex, visited)

    def dft_recursive_helper(self, curr_vertex, visited):
        visited.add(curr_vertex)
        print(curr_vertex)
        for neighbor in self.vertices[curr_vertex]:
            if neighbor not in visited:
                self.dft_recursive_helper(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        visited = set()
        queue = deque()
        queue.append([starting_vertex])
        while len(queue) > 0:
            currPath = queue.popleft()
            currNode = currPath[-1]
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.vertices[currNode]:
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    queue.append(newPath)
        return []

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = deque()
        stack.append([starting_vertex])
        visited = set()
        while len(stack) > 0:
            currPath = stack.pop()
            currNode = currPath[-1]
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.vertices[currNode]:
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    stack.append(newPath)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        visited = set()
        return self.dfs_recursive_helper([starting_vertex], destination_vertex, visited)

    def dfs_recursive_helper(self, curr_path, destination_vertex, visited):
        curr_vertex = curr_path[-1]
        if curr_vertex == destination_vertex:
            return curr_path
        visited.add(curr_vertex)
        for neighbor in self.vertices[curr_vertex]:
            if neighbor not in visited:
                newPath = list(curr_path)
                newPath.append(neighbor)
                res = self.dfs_recursive_helper(newPath, destination_vertex, visited)
                if len(res) > 0:
                    return res
        return []


# Destination city

"""
https://leetcode.com/problems/destination-city/

Understand

Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city.
Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Plan
1. Translate the problem into graph terminology
Vertex = a city
Edge = route from city to another city
Weights not needed

2. Build your graph
We can easily build a graph using adjacency lists from the input

3. Traverse your graph
Either BFT/DFT will work. You can start from any vertices.
If the current node we're at is not a key in the dictionary (graph), then it means it has
no outbound edges. That's the destination city
"""

from collections import deque

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        if len(paths) == 0:
            return ''
        graph = self.createGraph(paths)
        stack = deque()
        stack.append(paths[0][0])
        visited = set()
        while len(stack) > 0:
            curr = stack.pop()
            visited.add(curr)
            if curr not in graph:
                return curr
            else:
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return ''

    def createGraph(self, paths):
        graph = {}
        for edge in paths:
            origin, destination = edge[0], edge[1]
            if origin in graph:
                graph[origin].add(destination)
            else:
                graph[origin] = { destination }
        return graph


# Word Ladder

"""
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:

Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.

Sample:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
["hit", "hot", "dot", "dog", "cog"]

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
[]

1. Translate the problem into graph terminology
vertex - a word
edge - possible one letter transformation from a word to another word (undirected)
path - transformations of a word
weights - n/a

2. Build your graph
- we can create all possible transformations of beginWord and its transformation, but that would waste a lot of memory
- instead, we can determine which vertex to visit next if the transformation is in the wordList

3. Traverse the graph
- shortest = BFS
- we can traverse the graph using BFS and a queue
- use a set to avoid re-visiting nodes
- start from beginWord, and generate word transformations from it. enqueue nodes that are in the wordList
- keep track of the path we're currently on as we're traversing via a list
- once we find endWord, then we simply return the path to that node
"""

from collections import deque

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def findLadders(beginWord, endWord, wordList):
    words = set(wordList)
    visited = set()
    queue = deque()
    queue.append([beginWord])
    while len(queue) > 0:
        currPath = queue.popleft()
        currWord = currPath[-1]
        if currWord in visited:
            continue
        visited.add(currWord)
        if currWord == endWord:
            return currPath
        for i in range(len(currWord)):
            for letter in alphabet:
                transformedWord = currWord[:i] + letter + currWord[i + 1:]
                if transformedWord in words:
                    newPath = list(currPath)
                    newPath.append(transformedWord)
                    queue.append(newPath)
    return []

a = findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print(a)

b = findLadders("hit", "cog", ["hot","dot","dog","lot","log"])
print(b)