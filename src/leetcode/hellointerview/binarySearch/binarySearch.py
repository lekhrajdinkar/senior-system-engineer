from typing import List

class Template:
    #section::bruteForce::start
    def bruteForce(self, nums, target):
        for i in range(len(nums)):
            nxt = nums[i]
            if nxt == target:
                print(f"{target} found at {i} index")
                break
    #section::bruteForce::end

    #section::binarySearch::start
    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    #section::binarySearch::end

# ==================================================

class Solution:
    # section::section-875::start
    def minHarvestRate(self, apples, h):
        # Binary search on harvest rate: find minimum rate to finish in h hours
        def time_taken(rate):  # Calculate total time needed at this harvest rate
            time = 0
            for i in range(len(apples)):
                # Ceiling division: (apples[i] + rate - 1) // rate
                time += (apples[i] + rate - 1) // rate
                #time1 = apples[i]//rate # rate is 3 , for 7 apples 3,3,1 = 3 hr, for 6 apples 3,3 = 2 hr
                #time2 = [ 1 if apples[i]%rate !=0 else 0]
                #time = time1 + time2
            return time

        # Binary search bounds: minimum rate = 1, maximum rate = max apples
        left, right = 1, max(apples)

        # Binary search for minimum valid harvest rate
        while left < right:
            mid = (left + right) // 2
            if time_taken(mid) > h:
                left = mid + 1 # Rate too slow, need faster rate
            else:
                right = mid   # Rate is sufficient, try slower rate
        return left
    # section::section-875::end

    # section::section-33::start
    def search33(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:   # left half is sorted 💡
                if nums[left] <= target and target < nums[mid]:
                    # target is in the left half
                    right = mid - 1
                else:
                    # target is in the right half
                    left = mid + 1
            else:  # right half is sorted 💡
                if nums[mid] < target and target <= nums[right]:
                    # target is in the right half
                    left = mid + 1
                else:
                    # target is in the left half
                    right = mid - 1

        return -1
    # section::section-33::end


    # section::section-410::start
    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        pass
    # section::section-410::end


    # section::section-378::start
    def kthSmallest3(self, matrix: List[List[int]], k: int) -> int:
        pass
    # section::section-378::end


    # section::section-1011::start
    def kthSmallest4(self, matrix: List[List[int]], k: int) -> int:
        pass
    # section::section-1011::end

## ===========


find([5,6,76,89,23,0],89)
find([5,6,76,89,23,0],76)



