from collections import deque, defaultdict
# Vertices

# pare

# step 2 - traverse the graph
def earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)
    stack = deque()
    # node, distance from starting node
    stack.append((starting_node, 0))
    visited = set()
    EarliestAncestor = [starting_node, 0]

    # traversing the graph
    while len(stack) > 0:
        curr = stack.pop()
        currNode, distance = curr[0], curr[1]
        visited.add(curr)

        if currNode not in graph:
            if distance > EarliestAncestor[1]:
                EarliestAncestor = curr
            elif distance == EarliestAncestor[1] and currNode < EarliestAncestor[0]:
                EarliestAncestor = curr
            else:
                for ancestor in graph[currNode]:
                    if ancestor not in visited:
                        stack.append((ancestor, distance + 1))

    return EarliestAncestor[0] if EarliestAncestor != starting_node else -1

# step 1 - create the graph
def createGraph(edges):
    # every key i add to this dictionary, will have a default value of set{}

    graph = defaultdict(set)
    for edge in edges:
        ancestor, child = edge[0], edge[1]
        graph[child].add(ancestor)
    return graph
        