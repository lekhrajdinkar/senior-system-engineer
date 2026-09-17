# BFS : Graph
## Reference
- [graph.md](../../01_DS/03_graph.md)
- [BFS-on-BT.md](01_01_BFS-on-BT.md)
- https://www.hellointerview.com/learn/code/breadth-first-search/graphs-overview

---
## BFS :: Graph
[02_bfs_graph.excalidraw](../../draw/03/08_BFS/02_bfs_graph.excalidraw)

-  breadth-first search is also used to **traverse graphs.**
- implement BFS on both adjacency lists and matrices
- keep track of **visited nodes** to avoid infinite loops.

---
## BFS :: Graph (AdjList)
### tab:1 Basic
To traverse a graph represented with an adjacency list with BFS:
- Choose a **starting node** and add it to the queue.
  - eg: first item in adjList, `1`
- remove the node at the front of the queue and add it to the set of **visited nodes.**
- **Add the children/neighbors** of the node to the back of the queue, 
  - **if they haven't been visited yet**
- **Repeat** steps 2 and 3 until the queue is empty.

```python
# DS : Adjacency List
adjList = {
    "1": ["2", "4"],
    "2": ["1", "3"],
    "3": ["2", "4"],
    "4": ["1", "3", "5"],
    "5": ["4"]
}
start = "1"

from collections import deque
def bfs(start): 
  visited = set([start]) 
  queue = deque([start])
  while queue:
    node = queue.popleft()
    for neighbor in adjList[node]:
      if neighbor not in visited: # 👈
        visited.add(neighbor) # ⭐
        queue.append(neighbor) # ⭐
```

### tab:2 Extended
- having levels

```python
from collections import deque

def bfs_levels(graph, start):
    queue = deque([start])
    visited = set()
    visited.add(start)
    levels = []

    while queue:
        # === level Starts here === ⭐
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # === level ends here === ⭐
        levels.append(current_level)

    return levels
```

---
## BFS :: Graph (2D matrices)
### tab:1 basic
To traverse a graph represented as a matrix with BFS:
- Choose a starting node and add it to the queue 
  - eg: start =  top left node
- remove the node at the front of the queue and add it to the set of visited nodes.
- Add the four neighbors of the node to the back of the queue 
  - if they haven't been visited yet 
  - and are within the bounds of the matrix.
- Repeat steps 2 and 3 until the queue is empty.

```python
from collections import deque
def bfs(grid):
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # up, down, left, right
  queue = deque([(0, 0)]); visited = set()
  visited.add((0, 0))
  
  while queue:
    row, col = queue.popleft()
    # enqueue neighbors
    for dr, dc in directions:
      n_row = row + dr
      m_col = col + dc
      # check bounds and if neighbor is visited
      if 0 <= n_row < len(grid) \
                and 0 <= m_col < len(grid[0]) \
                and (n_row, m_col) not in visited:
        queue.append((n_row, m_col))
        visited.add((n_row, m_col))

```

### tab:2 extended
- having levels
- we can use it to find the shortest path between two nodes in a graph.

```python
from collections import deque

def bfs_level_by_level(matrix):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # start at the top-left corner
    queue = deque([(0, 0)]);  visited = set([(0, 0)])

    levels = []
    while queue:
        # === level Starts here === ⭐
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            row, col = queue.popleft()
            current_level.append((row, col))
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c))

        # === level Ends here === ⭐
        levels.append(current_level)

    return levels
```
---
## BFS vs DFS
- example: find shorted path

![img.png](img.png)
