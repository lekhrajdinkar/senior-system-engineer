# DSA: on Graph
## reference
- https://www.hellointerview.com/learn/code/depth-first-search/graphs-overview

---
## Graph Basic
[04_graph.excalidraw](../draw/03/07_DFS/04_graph.excalidraw)

- representations : 
  - adjacency lists 
  - 2d matrices
- Graphs consist of **nodes** (also frequently referred to as vertices), and **edges** that connect the nodes.
- graphs can be either directed or undirected.
- Nodes that are connected to each other via an edge are known as the **neighbors** of that node.
- A graph can contain **cycles**| A cycle is a path that starts and ends at the same node.
- A **connected graph** is a graph where there is a path between every pair of nodes
- A **disconnected graph** is a graph where there are at least two nodes that are not connected to each other by a path.
> 💡A tree is a connected graph with no cycles 

---
## DFS on graph
> DFS for a graph is conceptually similar to DFS on a binary tree. **Pattern**: 
> - connected components
> - boundary traversal
> - cycle detection

Graph problems **adds complexity**:
- you need to handle cycles,
- different representations (adjacency lists and matrices),
- and sometimes disconnected components.

```python
visited = set()
def dfs(node, visited):
    if node in visited:
        return
    # 💡 We don't need an explicit base case like we do in the trees
    
    # 💡 keep track of nodes we have already visited
    visited.add(node) 
    
    # 💡 so we need a 'for loop' to iterate over each neighbor rather
    # than making calls to the left and right children of the current node.
    for neighbor in node.neighbors:
        dfs(neighbor, visited)

# Handle disconnected components
for node in nodes:
     if node not in visited:
         dfs(node)
```

**Summary**
- Use a **set** to keep track of visited nodes.
- If you encounter, visited node **return immediately** without making any further recursive calls.
- Use a **for loop** to iterate over each neighbor of the current node, and recursively call dfs on each neighbor.

---
## Time and space Complexity
**DFS traversal**
- `O(N + M)` time and `O(N + M)` space
- where N is the number of nodes
- and M is the number of edges in the graph
- The space complexity is due to the **adjacency list** that stores the graph structure

---
## 1. representation: Adjacency Lists 
[Exercise-Graph-adjList.md](03_02_Exercise-Graph-adjList.md)
### tab:1 Example
- n = 4
- edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]
- node and its **neighbours**:
```adjList
adjList = 
{
  0: [1, 3, 2],
  1: [0, 2],
  2: [1, 3, 0],
  3: [2, 0]
}
```
### tab:2 build AdjList
```python
# build
def build_adj_list(n, edges):
    adj_list = {i: [] for i in range(n)}
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    return adj_list
```

### tab:3 DFS on AdjList (template)
```python
# DFS on adjList
def dfs(adjList: dict):
  if not adjList:
    return

  visited = set()
  def dfs_helper(node):
    if node in visited:
      return
    
    visited.add(node)
    
    for neighbor in adjList[node]:
      dfs_helper(neighbor)
    return
  
  # Handle disconnected components
  for node in adjList:
    if node not in visited:
      dfs_helper(node)
```

---
## 2. representation: 2D matrix grids
[Exercise-Graph-2d-matrices.md](03_03_Exercise-Graph-2d-matrices.md)
### tab:1 Example
- Another common way to represent a graph is as a matrix (2D-grid). 
- Each cell in the grid represents a node. | node: `(x,y)`
- The **neighbors** of each node are the cells that are adjacent to it 
  - so fixed at most `4` neighbors
  - `(x-1,y)`, `(x+1,y)` | left and right 
  - `(x,y-1)`, `(x,y+1)`| up and down

```visual
 grid = [
            [1, 0, 1],      
            [1, 0, 0],
            [0, 0, 1]
      ]
```
### tab:2 DFS on 2d-matrices
- DFS on a matrix is similar to DFS on an adjacency list
-  We still have to keep track of visited nodes, and we **recursively call DFS on each neighbor** of the current node.
- main difference is that each cell can have at most 4 neighbors (up, down, left, right)
- Use a `for loop ` to iterate over each neighbor of the current node, and recursively call

```python
def dfs(matrix):
  visited = set() # tuple (x,y) coordinate
  # up, down, left, right
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  def dfs_helper(r, c):
    if (r, c) in visited:
      return
    
    # check if the cell is out of bounds
    if (r < 0 or r >= len(matrix))   or   (c < 0 or c >= len(matrix[0])):
      return
    
    visited.add((r, c))
    # DFS on neighbour
    for dr, dc in directions: # run max 4 times
      dfs_helper(r + dr, c + dc)
        
    return
  
  dfs_helper(0, 0)
```
---
Short form:

@[code:section::section-template-1](../../../../src/leetcode/hellointerview/DFS/exercise-3.py)

### tab:3 visual
[06_graph_2d-matrices.excalidraw](../draw/03/07_DFS/06_graph_2d-matrices.excalidraw)

