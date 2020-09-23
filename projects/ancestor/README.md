# Earliest Ancestor

This is a take-home coding challenge from a top tech company. The spec is providied verbatim.


## Problem

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram and the sample input, 3 is a child of 1 and 2, and 5 is a child of 4:

```
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
```

Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.

```
Example input
  6

  1 3
  2 3
  3 6
  5 6
  5 7
  4 5
  4 8
  8 9
  11 8
  10 1
Example output
  10
```

Clarifications:
* The input will not be empty.
* There are no cycles in the input.
* There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
* IDs will always be positive integers.
* A parent may have any number of children.

Vertices

- Parents and kids

Edges

- path from parent to kids
- undirectional

{
  10 : {1, 3, 6}
  # 1: {3, 6}
  # 3: {6}
  # 6 : {} OLDEST ANCESTOR = 10 NO MATTER WHICH CHILD IS CHOSEN
  # 4 : {5, 6, 7, 8, 9}
  4 : {5, 6, 7, 8, 9}
  # 5 : {6, 7}
  7 : {}
  # 2 : {3, 6}
  11 : {8, 9}
  8: {9}
  9: {}

}

Type of graph to use. 

List adjacent matrix 

# Second Idea, use the child as the keys, and parents as values

## LEETCODE

        SA, SB = sum(A), sum(B)
        for x in A:
            for y in B:
                if x + (SB - SA)/2 == y:
                    return x, y

[[x,y] for x in A for y in B if x + (SB - SA)/2 == y ]

# from lecture

* Vertices = Person/ID
* edge = parent- child relationship
* path = ancestor tree

* Build a directed graph from child to parent

* traverse a person's family tree upwards to its farthest ancestor