# CSPT10 Graphs III
# Earliest Ancestor

"""
Understand
    1   2
     \ /
      3
       \
        6
input: [(1, 3), (2, 3), (3, 6)]

starting node: 6
output: 1 (1 and 2 are tied but 1 has a lower id)

starting node: 1
output: -1 (1 has no ancestor)

Plan
1. Translate the problem into graph terminology
vertex - a person (in this case, we're given their ids)
edge - parent-child relationship between two people
path - a person's family tree
weight - not needed, all edges are equal and have no value/cost related to them

2. Build your graph
Build a graph by using the parent-child relationships/edges we're given. Each node in the
graph will have an outgoing/directed edge to its parent/ancestor.

3. Traverse the graph
We traverse the graph while keeping track of the node's distances from the starting node
and keep track of the terminal node with the lowest id and greatest distance.
A terminal node will have no outgoing edges, meaning it has no more ancestors. A terminal node
doesn't mean it's the earliest ancestor though, so we need to consider the terminal node that is
the greatest distance from the starting node (that also has the lowest id).

In this case, we can use a depth-first traversal (DFT) to traverse all of the starting node's
ancestors and return the earliest one with the lowest id.
"""
from collections import deque
from collections import defaultdict

def earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)
    # A tuple with a node and its distance from the starting node
    # At the beginning, the starting node's earliest ancestor is itself
    earliestAncestor = (starting_node, 0)
    stack = deque()
    stack.append((starting_node, 0))
    visited = set()
    while len(stack) > 0:
        curr = stack.pop()
        currNode, distance = curr[0], curr[1]
        visited.add(curr)

        # This checks if the node is a terminal node
        if currNode not in graph:
        # Only consider terminal nodes that have a greater distance than the ones we've found so far
            if distance > earliestAncestor[1]:
                earliestAncestor = curr
            # If there's a tie then choose the ancestor with the lower id
            elif distance == earliestAncestor[1] and currNode < earliestAncestor[0]:
                earliestAncestor = curr
        else:
            for ancestor in graph[currNode]:
                if ancestor not in visited:
                    stack.append((ancestor, distance + 1))

    # If the starting node's earliest ancestor is itself, then just return -1
    return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1

# Creates a graph where the keys are a node and its values are its ancestors
def createGraph(edges):
    # This convenience method simply allows us to initialize default values when assigning
    # a key to a dictionary. In this case, the default value for a new key is an empty set
    graph = defaultdict(set)
    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)
    return graph

# Count Islands

"""
https://leetcode.com/problems/number-of-islands/submissions/

Understand

normal grid w/ multiple islands
["1","1","1"]
["1","0","0"]
["0","1","0"]

output = 2

empty grid
["0","0","0"]
["0","0","0"]
["0","0","0"]

output = 0

grid that is an entire island
["1","1","1"]
["1","1","1"]
["1","1","1"]

output = 1

Plan
Traverse the grid via DFS whenever you find an island.
Find the connected components/connecting islands and mark them as visited so you don't overcount them.
Runtime: O(m * n)
Space: O(m * n)
"""
from collections import deque

class Solution:
    res = 0

    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        width, height = len(grid[0]), len(grid)
        visited = [[False] * width for x in range(height)]
        for y in range(height):
            for x in range(width):
                if grid[y][x] == '1' and not visited[y][x]:
                    self.res += 1
                    self.iterativeDFS(grid, visited, x, y)
        return self.res

    def iterativeDFS(self, grid, visited, x, y):
        width, height = len(grid[0]), len(grid)
        stack = deque()
        stack.append((x, y))
        while len(stack) > 0:
            x, y = stack.pop()
            if visited[y][x]:
                continue
            visited[y][x] = True
            if x - 1 >= 0 and grid[y][x - 1] == '1':
                stack.append((x - 1, y))
            if x + 1 < width and grid[y][x + 1] == '1':
                stack.append((x + 1, y))
            if y - 1 >= 0 and grid[y - 1][x] == '1':
                stack.append((x, y - 1))
            if y + 1 < height and grid[y + 1][x] == '1':
                stack.append((x, y + 1))

    def recursiveDFS(self, grid, visited, x, y):
        width, height = len(grid[0]), len(grid)
        if x < 0 or y < 0 or x >= width or y >= height or grid[y][x] == '0' or visited[y][x]:
            return
        visited[y][x] = True
        self.dfs(grid, visited, x + 1, y)
        self.dfs(grid, visited, x - 1, y)
        self.dfs(grid, visited, x, y + 1)
        self.dfs(grid, visited, x, y - 1)

# Social Graph

def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        for i in range(0, num_users):
            self.add_user(f"User {i}")
        possible_friendships = []
        # Generate all possible friendships possible
        for user_id in self.users:
            # To avoid duplicating friendships, create friendships from user_id + 1
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))

        # Shuffle the entire array of possible friendships
        random.shuffle(possible_friendships)

        # Select the first num_users * avg_friendships / 2
        # We / 2 because a friendship is a bidirectional edge (we're essentially adding two edges)
        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])