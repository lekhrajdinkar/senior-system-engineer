from collections import deque
import heapq

class Solution:
    # section:util-1:start
    def build_adj_list_2(self, n, edges, start_from_one = False): # ⭐DAG
        if start_from_one:
            adj_list = {i: [] for i in range(1,n+1)}
        else:
            adj_list = {i: [] for i in range(n)}
        # adj_list = {i: [] for i in range(n)}
        for u, v, w in edges:
            adj_list[u].append((v,w))
        print(f"\n 🟡build_adj_list for weighted graph \n- edges u,v,w : {edges} \n- adj_list: u -> [(v1,w1),...]) : \n{adj_list} \n{'-'*3}")
        return adj_list

    """
     build_adj_list for weighted graph 
        - edges u,v,w : [[2, 1, 1], [2, 3, 1], [3, 4, 1]] 
        - adj_list: u -> [(v1,w1),...]) : 
        { 
            1: [], 
            2: [(1, 1), (3, 1)], 
            3: [(4, 1)], 
            4: [] 
        } 
    """

    def build_adj_list(self, n, edges): # ⭐undirected
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        print(f"\n 🟡build_adj_list for un-weighted graph \n- edges: {edges} \n- adj_list: \n{adj_list} \n{'-'*3}")
        return adj_list

    """
    build_adj_list for un-weighted graph
    - edges u,v: [ ... ]
    - adj_list = {
        0: [1, 2],
        1: [3],
        2: [1, 3],
        3: [4],
        4: []
    }
    """
    # section:util-1:end

    # section:short_path_bfs:start
    # ⭐ short_path_bfs
    def bfs(self, graph: dict, source: int):
        distances = {node: float('inf') for node in graph}
        distances[source] = 0  # { node1:0, node2:inf, ....}
        queue = deque([source])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if distances[neighbor] == float('inf'):
                    distances[neighbor] = distances[node] + 1
                    queue.append(neighbor)
        return distances
    # section:short_path_bfs:end

    # section:short_path_dijkstra:start
    # ⭐ short_path_dijkstra | STANDARD VERSION | multiple dst
    def dijkstra(self, adjList:dict, source:int): # graph is "adjList" 👈
        distances = {node: float('inf') for node in adjList} # result
        distances[source] = 0 # { node1:0, node2:inf, node3:inf, ... }
        heap = [(0, source)] # state: (distance2Node, node) | 0 because from and to are same

        while heap:
            dist2Node, node = heapq.heappop(heap) # heap will pop next smallest w
            if dist2Node > distances[node]: continue # ignore long path

            # explore short path, further until reached all other nodes.
            for neighbor, weight in adjList[node]:
                dist2neighbor = dist2Node + weight
                if dist2neighbor < distances[neighbor]:
                    distances[neighbor] = dist2neighbor # update result
                    heapq.heappush(heap,(dist2neighbor, neighbor)) # so that can further explore it.

        print(f"dijkstra | distances: {distances}")
        return distances
    # section:short_path_dijkstra:end

    # section:short_path_dijkstra_2:start
    # ⭐ short_path_dijkstra_2 | extended VERSION | Single dst
    # try to reach node with multiple path, capture steps taken, plus distance covered
    def dijkstra_2(self, adjList: dict, source:int, dst:int, max_stop:int):
        heap = [(0, source, 0)] # state: (dist2Node, node, stopCountToReachToNode) Also store steps taken
        best_routes = {} # key: (node, stopCountToReachToNode) | value: dist2Node

        while heap:
            dist2Node, node, stopCountToReachToNode = heapq.heappop(heap) # heap will pop next smallest w

            if node == dst: return dist2Node # result
            if stopCountToReachToNode > max_stop: continue # 🔺 ignore-1

            # 🔺ignore-2 dist2Node with same Steps is greater, meaning longer path. then ignore it,
            # else track the smallest path found so far
            key=(node, stopCountToReachToNode)
            if key in best_routes and best_routes[key] <= dist2Node: continue

            best_routes[(node, stopCountToReachToNode)] = dist2Node

            # explore neighbors
            for neighbor, weight in adjList[node]:
                heapq.heappush(heap,(dist2Node + weight, neighbor, stopCountToReachToNode+1)) # increment stop by 1 ⭐

        return -1
    # section:short_path_dijkstra_2:end

    # ===============================================

    # section:problem-743:start
    # n --> no of nodes
    def networkDelayTime(self, times: list[list[int]], n: int, src: int) -> int:
        adjList = self.build_adj_list_2(n,times,True)
        res = self.dijkstra(adjList,src)
        minTime = -1 if float('inf') in res.values() else max(res.values())
        print(f"networkDelayTime: {minTime}")
        return minTime
    # section:problem-743:end

    # section:problem-787:start
    # n --> no of nodes
    # k --> max stops allowed
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adjList = self.build_adj_list_2(n,flights)
        res = self.dijkstra_2(adjList,src,dst,k)
        return -1
    # section:problem-787:end

    # section:problem-1631:start
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # shift
        rows = len(heights)
        cols= len(heights[0])



        start = (0,0)

        for nr, nc in directions:
            r + nr , c + nc





        for r in range(rows):
            for c in range(cols):




    # section:problem-1631:end

    # section:problem-1334:start
    def problem1334(self):
        pass
    # section:problem-1334:end

if __name__ == "__main__":
    def networkDelayTime_test():
        Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, src = 2)
        Solution().networkDelayTime([[1,2,1]], n = 2, src = 1)
        Solution().networkDelayTime([[1,2,1]], n = 2, src = 2)

    def findCheapestPrice_test():
        Solution().findCheapestPrice( n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1)

    # networkDelayTime_test()   # problem-743
    findCheapestPrice_test()    # problem-787