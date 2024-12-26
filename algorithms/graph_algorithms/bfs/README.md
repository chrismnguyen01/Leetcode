# Breadth First Search

## Description
Breadth-First Search (BFS) is an algorithm used to traverse or search through a graph or tree data structure. It starts at a root node (or any arbitrary node in the graph), explores all its neighbors, then moves on to the next level of neighbors, and continues this process until all nodes are visited.

Key characteristics of BFS:
    - Level-order traversal: It explores nodes in layers (level by level).
    - Queue: BFS uses a queue data structure to store the nodes to be explored.
    - Optimal for finding the shortest path in an unweighted graph.

BFS Algorithm Steps:
    - Start with a node and mark it as visited.
    - Enqueue the node into a queue.
    - While the queue is not empty:
    - Dequeue the front node.
    - Visit all its unvisited neighbors, mark them as visited, and enqueue them.

### Shell Code

#### Queues

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    # While there are still nodes in the queue
    while queue:
        # Pop off the queue
        node = queue.popleft()
        print(node, end=" ")  # Process the node
        # Add each neighbor to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```
