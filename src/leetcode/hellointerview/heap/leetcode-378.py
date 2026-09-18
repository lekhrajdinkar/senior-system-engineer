from typing import List, Optional
import heapq

#section::section-378-example::start
"""
matrix = [
    [ 1, 5, 9],
    [10,11,13],
    [12,13,15]]
k = 8
"""
#section::section-378-example::end

class Solution:
    #section::section-378-1::start
    # ⭐inspired from problem : 23 (heap section)
    def kthSmallest_1(self, matrix: List[List[int]], k: int) -> int:
        # handle null/empty scenario
        if not matrix: return -1
        non_empty = [arr for arr in matrix if arr]
        if not non_empty: return -1

        # 1, heapify ---
        heap = []
        for i,arr in enumerate(non_empty):
            heapq.heappush(heap, (arr[0], i, arr)) # tie-breaker i

        # 2. process ---
        count = 0
        while heap:
            arr_0, i, arr = heapq.heappop(heap)
            count += 1

            if count == k:
                print(f"✔️378(1): {k} smallest elemnet from matrix: {arr_0}")
                return arr_0

            # Push next element from same row
            #if arr[1:]:
            if arr[1:]:
                arr[:] = arr[1:]
                heapq.heappush(heap, ( arr[0], i, arr))

        return -1
    #section::section-378-1::end

    #section::section-378-2::start
    def kthSmallest_2(self, matrix: List[List[int]], k: int) -> int:
        # handle null/empty scenario
        if not matrix: return -1
        non_empty = [arr for arr in matrix if arr]
        if not non_empty: return -1

        # 1, heapify ---
        heap = []
        for i,arr in enumerate(matrix):
            heapq.heappush(heap, (arr[0], i, 0)) # tie-breaker i (first item in row, row, col)

        # 2. process ---
        count = 0
        while heap:
            value, i, j = heapq.heappop(heap)
            count += 1

            if count == k:
                print(f"✔️378(2): {k} smallest elemnet from matrix: {value}")
                return value

            # Push next element from same row
            # if arr[1:]: #  🔺🔺 This modifies the original row and repeatedly creates slices.
            next_col = j+1
            if next_col< len(matrix[i]): # ✅
                heapq.heappush(heap, ( matrix[i][next_col], i, next_col))

        return -1
    #section::section-378-2::end

# ====== Run ====

Solution().kthSmallest_1([[1,5,9],[10,11,13],[12,13,15]],8)
Solution().kthSmallest_2([[1,5,9],[10,11,13],[12,13,15]],8)

