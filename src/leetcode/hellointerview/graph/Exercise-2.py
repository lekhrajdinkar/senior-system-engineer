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
    # dijkstra 2
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # shift
        rows,cols = len(heights),len(heights[0]); print(f"rows: {rows}, cols: {cols}")
        heap = [(0,0,0,0)] # (effort, nodeHeight, r, c)
        best_routes = {}

        while heap:
            effort,nodeHeight,r,c = heapq.heappop(heap) #; print( ">> ", nodeHeight,effort,r,c)

            if (r,c) == (rows-1, cols-1):
                print(f"final result, {effort}");return effort

            key = (r, c)
            if key in best_routes and best_routes[key] <= effort: continue
            best_routes[(r, c)]=effort

            print(f"current node at ({r},{c}) with height: {heights[r][c]} and best effort to reach {effort} ")
            for dr,dc in directions:
                rn,cn = r+dr,c+dc
                if (0 <= rn < rows) and (0 <= cn < cols):
                    edge_effort = abs(heights[rn][cn] - heights[r][c])
                    #The key difference from normal Dijkstra
                    # - new_distance = distance + weight
                    # - new_effort = max(effort, edge_effort)
                    heapq.heappush(heap,(max(effort, edge_effort),heights[rn][cn],rn,cn))
                    #heapq.heappush(heap,(edge_effort,heights[rn][cn],rn,cn))

        print(f"final result : 0");return 0
    # section:problem-1631:end

    # section:problem-1631-1:start
    # used queue instead of min-heap. my attempt-1
    def minimumEffortPath_1(self, heights: list[list[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # shift
        rows,cols = len(heights),len(heights[0]); print(f"rows: {rows}, cols: {cols}")
        visited = [(0,0)];  maxEffort = 0 ; queue = deque([(0,0,0,0)]) # (nodeHeight, r, c, effort)

        while queue:
            nodeHeight,r,c,effort = queue.popleft()
            maxEffort = max(maxEffort,effort)

            if (r,c) == (rows-1, cols-1):
                print(f"final result, maxEffort : {maxEffort}")
                return maxEffort

            print(f"current node at ({r},{c}) with height: {heights[r][c]}")
            next_dr, next_dc, next_effort, minH =  0,0,0,float('inf')
            for dr,dc in directions:
                    rn,cn = r+dr,c+dc
                    if (0 <= rn < rows) and (0 <= cn < cols) and (rn,cn) not in visited:
                            effort = abs(heights[rn][cn] - heights[r][c])

                            if effort < minH:
                                next_dr, next_dc, next_effort = rn, cn, effort
                                minH = effort

                            print(f"\t- checking its neighbour at ({rn},{cn}) of height {heights[rn][cn]} | minH: {minH}")
                            visited.append((rn,cn))

            queue.append((heights[next_dr][next_dc],next_dr,next_dc,next_effort))
            print(f"\tNeighbour ({next_dr},{next_dc}) added to queue next : {queue} | max effort : {maxEffort}")
        print(f"final result, maxEffort : {maxEffort}")
        return maxEffort
    # section:problem-1631-1:end

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

    def minimumEffortPath_1_test():
        Solution().minimumEffortPath_1([[4,3,2], [2,6,3], [3,2,1]])
        Solution().minimumEffortPath_1([[1,10,2], [2,3,3], [3,2,1]]) # hi
        Solution().minimumEffortPath_1([[1,2,2],[3,8,2],[5,3,5]]) # lc

    def minimumEffortPath_test():
        #Solution().minimumEffortPath([[4,3,2], [2,6,3], [3,2,1]])
        #Solution().minimumEffortPath([[1,10,2], [2,3,3], [3,2,1]]) # hi
        Solution().minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]) # lc
        Solution().minimumEffortPath([[1,2,3],[3,8,4],[5,3,5]]) # lc
        Solution().minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]) # lc

    # ====================================
    # networkDelayTime_test()   # problem-743
    # findCheapestPrice_test()    # problem-787
    #minimumEffortPath_1_test()
    minimumEffortPath_test()
