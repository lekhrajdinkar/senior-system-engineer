from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)      # Minimum possible answer
        right = sum(nums)     # Maximum possible answer
        step = 1

        print(f"\n{'=' * 60}")
        print(f"nums = {nums}, k = {k}")
        print(f"Search Range: [{left}, {right}]")
        print(f"{'=' * 60}")

        while left < right:
            mid = (left + right) // 2

            print(f"\n🔍 Step {step}: Range [{left}, {right}] → mid = {mid}")

            if self.canSplit(nums, k, mid):
                print(f"✅ {mid} WORKS → search smaller → right = {mid}")
                right = mid
            else:
                print(f"❌ {mid} FAILS → need larger → left = {mid + 1}")
                left = mid + 1

            step += 1

        print(f"\n{'=' * 60}")
        print(f"🎯 FINAL ANSWER = {left}")
        print(f"{'=' * 60}")

        return left


    def canSplit(self, nums: List[int], k: int, max_sum: int) -> bool:
        subarrays = 1
        current_sum = 0
        groups = [[]]   # Only for visualization

        print(f"   Testing max_sum = {max_sum}")

        for num in nums:
            # Adding num would exceed max_sum → create new subarray
            if current_sum + num > max_sum:
                print(f"   {current_sum} + {num} > {max_sum} → NEW GROUP")

                subarrays += 1
                current_sum = num
                groups.append([num])
            else:
                current_sum += num
                groups[-1].append(num)

        # Visualize how the array was split
        visual = " | ".join(
            f"{group}={sum(group)}"
            for group in groups
        )

        print(f"   Split: {visual}")
        print(f"   Groups: {subarrays}, Allowed: {k}")

        return subarrays <= k

# =============

nums = [7, 2, 5, 10, 8]
k = 2

Solution().splitArray(nums, k)

"""

============================================================
nums = [7, 2, 5, 10, 8], k = 2
Search Range: [10, 32]
============================================================

🔍 Step 1: Range [10, 32] → mid = 21
   Testing max_sum = 21
   14 + 10 > 21 → NEW GROUP
   Split: [7, 2, 5]=14 | [10, 8]=18
   Groups: 2, Allowed: 2
✅ 21 WORKS → search smaller → right = 21

🔍 Step 2: Range [10, 21] → mid = 15
   Testing max_sum = 15
   14 + 10 > 15 → NEW GROUP
   10 + 8 > 15 → NEW GROUP
   Split: [7, 2, 5]=14 | [10]=10 | [8]=8
   Groups: 3, Allowed: 2
❌ 15 FAILS → need larger → left = 16

🔍 Step 3: Range [16, 21] → mid = 18
   Testing max_sum = 18
   14 + 10 > 18 → NEW GROUP
   Split: [7, 2, 5]=14 | [10, 8]=18
   Groups: 2, Allowed: 2
✅ 18 WORKS → search smaller → right = 18

🔍 Step 4: Range [16, 18] → mid = 17
   Testing max_sum = 17
   14 + 10 > 17 → NEW GROUP
   10 + 8 > 17 → NEW GROUP
   Split: [7, 2, 5]=14 | [10]=10 | [8]=8
   Groups: 3, Allowed: 2
❌ 17 FAILS → need larger → left = 18

============================================================
🎯 FINAL ANSWER = 18
============================================================

"""