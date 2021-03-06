"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
from collections import  deque

class Graph:

    def __init__(self):
        self.vertices = {}

    def __repr__(self):
        return str(self.vertices)

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id] if vertex_id in self.vertices else set()

    def dft(self, starting_vertex):
        visited = set()
        stack = deque()
        stack.append(starting_vertex)
        while len(stack) > 0:
            currNode = stack.pop()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.get_neighbors(currNode):
                    stack.append(neighbor)

    def bft(self, starting_vertex):
        visited = set()
        queue = deque()
        queue.append(starting_vertex)
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode not in visited:
                visited.add(currNode)
                print(currNode)
                for neighbor in self.get_neighbors(currNode):
                    queue.append(neighbor)

    # Returns path from starting vertex to destination vertex
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        
        stack = deque()
        # Each element in the stack is the current path e.g [1, 2, 3..]
        stack.append([starting_vertex])
        visited = set()
        while len(stack) > 0:
            currPath = stack.pop() # [1, 2, 3]
            currNode = currPath[-1] # 3
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.get_neighbors(currNode):
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    stack.append(newPath)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = set()
        return self.dfs_recursive_helper([starting_vertex], destination_vertex, visited)
    
    # returns path from starting vertex, to dest vertex else returns an empty list
    def dfs_recursive_helper(self, curr_path, destination_vertex, visited):
        curr_vertex = curr_path[-1]
        if curr_vertex ==  destination_vertex:
            return curr_path

        visited.add(curr_vertex)

        for neighbor in self.get_neighbors(curr_vertex):
            if neighbor not in visited:
                newPath = list(curr_path)
                newPath.append(neighbor)
                res = self.dfs_recursive_helper(newPath, destination_vertex, visited)
                if len(res) > 0:
                    return res

        return []


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        stack = deque()
        # Each element in the stack is the current path e.g [1, 2, 3..]
        stack.append([starting_vertex])
        visited = set()
        while len(stack) > 0:
            currPath = stack.popleft() # [1, 2, 3]
            currNode = currPath[-1] # 3
            if currNode == destination_vertex:
                return currPath
            if currNode not in visited:
                visited.add(currNode)
                for neighbor in self.get_neighbors(currNode):
                    newPath = list(currPath)
                    newPath.append(neighbor)
                    stack.append(newPath)

    #def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(f'Graph vertices {graph.vertices} \n ')

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print(f"breath first traversal")
    graph.bft(1)
    '''
    
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print(f"\ndepth first traversal")
    graph.dft(1)

    print(f"\ndepth first traversal recursive")
    #graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(f'\nbreath first search{graph.bfs(1, 6)} \n')

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    #print(graph.dfs(1, 6))
    #print(graph.dfs_recursive(1, 6))
    # print(graph.dfs(1, 6))
    print(f'Graph depth first search {graph.dfs(1, 6)} \n ')
    print(f'Graph depth first search recursive {graph.dfs_recursive(1, 6)} \n ')


    #graph.bfs(1, 6)
