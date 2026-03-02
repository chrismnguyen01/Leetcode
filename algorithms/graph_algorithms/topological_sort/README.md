# Topological Sort

## Description

Topological Sort is an algorithm used to order the nodes of a Directed Acyclic Graph (DAG) such that for every directed edge u → v, node u appears before v in the ordering. It is used when solving problems involving dependencies, where certain tasks must be completed before others.

Topological sorting is commonly applied in:
- Course scheduling (prerequisites)
- Build systems and compilation order
- Task scheduling
- Dependency resolution systems

Key characteristics of Topological Sort:
- Directed graph only
- Graph must be acyclic (no cycles)
- Produces a linear ordering of nodes
- Uses either BFS (Kahn’s Algorithm) or DFS
- If a cycle exists, no valid ordering is possible

Topological Sort Algorithm Steps (Kahn’s Algorithm – BFS):
- Compute the in-degree (number of incoming edges) for each node.
- Add all nodes with in-degree 0 to a queue.
- While the queue is not empty:
- Remove a node from the queue.
- Add it to the result.
- Decrease the in-degree of its neighbors.
- If a neighbor’s in-degree becomes 0, add it to the queue.
- If all nodes are processed → valid topological order.
- If not → cycle detected.

### Shell Code

#### BFS (Kahn’s Algorithm)

```python
from collections import deque

def topological_sort(graph):
    """
    Topological Sort using Kahn's Algorithm (BFS).
    
    Arguments:
    graph -- adjacency matrix (2D list) representing a directed graph
    """
    n = len(graph)
    
    # Compute in-degrees
    indegree = [0] * n
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                indegree[j] += 1

    # Queue for nodes with in-degree 0
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        # Reduce in-degree of neighbors
        for i in range(n):
            if graph[node][i] == 1:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

    # Detect cycle
    if len(topo_order) != n:
        print("Cycle detected. No valid topological ordering.")
        return []

    return topo_order
```

#### DFS (Recursive)

```python
def topological_sort(graph):
    """
    Topological Sort using DFS.
    
    Arguments:
    graph -- adjacency matrix (2D list) representing a directed graph
    """
    n = len(graph)
    visited = [0] * n  # 0 = unvisited, 1 = visiting, 2 = visited
    stack = []

    def dfs(v):
        if visited[v] == 1:
            return False  # cycle detected
        if visited[v] == 2:
            return True   # already processed

        visited[v] = 1

        for i in range(n):
            if graph[v][i] == 1:
                if not dfs(i):
                    return False

        visited[v] = 2
        stack.append(v)
        return True

    for i in range(n):
        if visited[i] == 0:
            if not dfs(i):
                print("Cycle detected. No valid topological ordering.")
                return []

    return stack[::-1]  # reverse to get topological order
```