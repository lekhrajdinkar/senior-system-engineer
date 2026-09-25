from typing import List, Optional
import heapq


# section::section-215::start
def findKthLargest(nums: List[int], k: int) -> int:
    heap = nums[:k]
    heapq.heapify(heap)

    # iterate through the remaining elements
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    print("✔️ 215.findKthLargest :: ", nums, k, "| RESULT: ",heap[0])
    return heap[0]
# section::section-215::end

# section::section-973::start
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
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

# section::section-658::start
def findClosestElements(arr: List[int], k: int, x: int) -> List[int]:
    # convert
    distances = [ (-abs(x-point),point) for point in arr ]
    heap = distances[:k]
    heapq.heapify(heap)

    # iterate through the remaining elements
    for num in distances[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)

    res = [x for distance, x in heap]
    res.sort()
    print(f"\n✔️ 658 findClosestElements:  \narr: {arr} | k : {k} | x (target): {x} \ndistances: {distances}  \nheap: {heap} \nres:  {res} ")
    return res
# section::section-658::end

# section::section-23::start

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # handle null/empty scenario
    if not lists: return None
    non_empty = [head for head in lists if head]
    if not non_empty: return None
    # ---
    current =  ListNode(0,None)
    start = current # will return this

    heap = []
    for i,head in enumerate(non_empty):
        heapq.heappush(heap, (head.val, head)) # tie-breaker i
        # If two nodes have the same value, Python tries to compare the ListNode objects.
        # use a unique index as a tie-breaker. 👈👈
        # Python's heap compares tuple elements from left to right.
        # heapq.heappush(heap, (head.val, i, head))

    print(heap)

    while heap:
        # poppedItemVal, poppedItem  = heapq.heappop(heap)
        poppedItemVal, i, poppedItem  = heapq.heappop(heap)
        current.next = poppedItem # chain it

        # push next item
        nextNode = poppedItem.next
        if nextNode:
            # heapq.heappush(heap, ( nextNode.val, nextNode))
            heapq.heappush(heap, ( nextNode.val, i, nextNode))

        current = current.next # move pointer >>

    return start.next
# section::section-23::end

# section::section-295::start
# input:
#   ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
#   [[],[1],[2],[],[3],[]]
# output: [null,null,null,1.50000,null,2.00000]
import heapq
class MedianFinder:
    def __init__(self):
        self.arr_l = [] # max heap (negative values)
        self.arr_r = [] # min heap
        heapq.heapify(self.arr_l)
        heapq.heapify(self.arr_r)

    def addNum(self, num: int) -> None: # O(log n) 💡💡
        # insert
        #if num <= -self.arr_l[0]:
        if not self.arr_l or num <= -self.arr_l[0]:
            heapq.heappush(self.arr_l, -num)
        else:
            heapq.heappush(self.arr_r, num)

        # balance
        if len(self.arr_r) > len(self.arr_l):
            num = heapq.heappop(self.arr_r)
            heapq.heappush(self.arr_l, -num)

        elif len(self.arr_l) > len(self.arr_r) + 1:
            num = -heapq.heappop(self.arr_l)
            heapq.heappush(self.arr_r, num)

    def findMedian(self) -> float:
        if len(self.arr_l) > len(self.arr_r):
            return -self.arr_l[0]
        else:
            return ( -self.arr_l[0 ] + self.arr_r[0] ) / 2
# section::section-295::end

# section::section-295-brute::start
# BruteForce
class MedianFinder2:
    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort() # 🔺🔺 O (n log n) eating time here

    def findMedian(self) -> float:
        l = len(self.arr)
        if l % 2 == 0: # even |  ( mid, mid+1 ) / 2
            mid = (l // 2 )
            median = ( self.arr[mid-1] + self.arr[mid] ) / 2 # since are 1 less from len, hence -1
            print(median)
            return median
        else: # odd | mid
            mid = (l // 2 ) +1
            return self.arr[mid-1]
# section::section-295-brute::end

# =================
findKthLargest([5, 3, 2, 1, 4],2)
# kClosest()
findClosestElements(arr = [1,2,3,4,5], k = 4, x = 3)
findClosestElements(arr = [5, 6, 7, 8, 9], k = 2, x = 10)