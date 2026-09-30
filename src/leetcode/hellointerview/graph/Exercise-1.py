from collections import deque

class Solution:
    # section:util-1:start
    def build_adj_list(self, n, edges):
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        return adj_list

    # from edges
    def indegree(self, n, edges) -> list[int]:
        indegree = [0] * n
        for u, v in edges:
            indegree[v] += 1
        return indegree

    # from adjList
    def indegree2(self, n,adj_list):
        indegree = [0] * n
        for u in adj_list:
            for v in adj_list[u]:
                indegree[v] += 1
    # section:util-1:end

    # section:topological_sort:start
    # ⭐ Kahn Algo
    def topological_sort(self, n, edges):
        # 1. calculate indegree of each node
        indegree = self.indegree(n,edges)
        adj_list = self.build_adj_list(n,edges)

        # 2. Add all nodes with an indegree of 0 to a queue.
        queue = deque([u for u in range(n) if indegree[u] == 0])

        order = []
        while queue: # 6. Repeat until empty
            u = queue.popleft() # 3. Dequeue the first node from the queue and add it to the topological order (result arr)
            order.append(u)

            for v in adj_list.get(u, []): #  4. For each neighbor of the node,
                indegree[v] -= 1 # decrement its indegree by 1.
                if indegree[v] == 0: queue.append(v) # 5. If the neighbor's indegree is now 0, add it to the queue.

        return order if len(order) == n else []
    # section:topological_sort:end

    # ===============================================

    # section:problem-207:start
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        res = self.topological_sort(numCourses, prerequisites)
        return True if len(res) == numCourses else False
    # section:problem-207:end

    # section:problem-210:start
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        res = self.topological_sort(numCourses, prerequisites)
        return res[::-1] if len(res) == numCourses else []
    # section:problem-210:end

    # section:problem-743:start
    def problem743(self):
        pass
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