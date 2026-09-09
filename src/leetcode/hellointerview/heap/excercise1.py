from typing import List

# section::section-215::start
def findKthLargest(nums: List[int], k: int) -> int:
    import heapq
    heap = nums[:k]
    heapq.heapify(heap)

    # iterate through the remaining elements
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    print("✔️ 215.findKthLargest :: ", nums, k, "| RESULT: ",heap[0])
    return heap[0]

findKthLargest([5, 3, 2, 1, 4],2)
# section::section-215::start

# section::section-973::start
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    import heapq
    import math

    # convert
    nums = [( -(point[0]*point[0] + point[1]*point[1]),
              point[0],
              point[1]) for point in points]
    print(nums)

    heap = nums[:k]
    heapq.heapify(heap)

    # iterate through the remaining elements
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

    print(heap, nums )
    return [[x, y] for distance, x, y in heap]
# section::section-973::end