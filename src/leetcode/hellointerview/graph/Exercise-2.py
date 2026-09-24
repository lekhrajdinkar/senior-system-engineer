from collections import deque
import heapq

class Solution:
    # section:util-1:start
    # ⭐ edge = [[2,1,1],[2,3,1],[3,4,1]] # u,v,w
    def build_adj_list_2(self, n, edges): # DAG
        adj_list = {i: [] for i in range(1,n+1)}
        for u, v, w in edges:
            adj_list[u].append((v,w))
        return adj_list

    def build_adj_list(self, n, edges): # undirected
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        return adj_list
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
    # ⭐ short_path_dijkstra
    def dijkstra(self, graph:dict, source:int):
        distances = {node: float('inf') for node in graph} # result
        distances[source] = 0 # { node1:0, node2:inf, ....}
        heap = [(0, source)]
        #print(f"distances: {distances}")

        while heap:
            dist2Node, node = heapq.heappop(heap) # heap will pop next smallest
            if dist2Node > distances[node]: continue # ignore long path

            # explore short path further
            for neighbor, weight in graph[node]:
                dist2neighbor = dist2Node + weight
                if dist2neighbor < distances[neighbor]:
                    distances[neighbor] = dist2neighbor # update result
                    heapq.heappush(heap,(dist2neighbor, neighbor)) # so that can further explore it.

        print(f"distances: {distances}")
        return distances
    # section:short_path_dijkstra:end

    # ===============================================

    # section:problem-743:start
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adjList = self.build_adj_list_2(n,times)
        res = self.dijkstra(adjList,k)
        minTime = -1 if float('inf') in res.values() else max(res.values())
        print(f"networkDelayTime: {minTime}")
    # section:problem-743:end

    # section:problem-787:start
    def problem787(self):
        pass
    # section:problem-787:end

    # section:problem-1631:start
    def problem1631(self):
        pass
    # section:problem-1631:end

    # section:problem-1334:start
    def problem1334(self):
        pass
    # section:problem-1334:end

if __name__ == "__main__":
    Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)
    Solution().networkDelayTime([[1,2,1]], n = 2, k = 1)
    Solution().networkDelayTime([[1,2,1]], n = 2, k = 2)