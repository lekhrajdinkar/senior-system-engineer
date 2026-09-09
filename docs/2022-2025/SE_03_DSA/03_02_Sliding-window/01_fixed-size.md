# Sliding window: fixed size
## Reference
- https://www.hellointerview.com/learn/code/sliding-window/fixed-length

## Template / pattern
> pattern: searching for a continuous subarray/substring
- Sliding windows can be either **variable** or **fixed length**
- but the implementation is a bit simpler.
- during each iteration, you both add and remove an element from the window to maintain its fixed size.
- 2 pointers: `start` and `ends`. 
  - both moves with same delta (for fixed)
  - both moves at different delta (in variable window) 
- compare template with [varying-size window](02_varying-size.md#template-)

[02_01_max_window_sum.excalidraw](../draw/03/02/02_01_max_window_sum.excalidraw)

```python
def fixed_length_sliding_window(nums, k):
    state = {} # choose appropriate data structure
    start = 0
    max_ = 0
    for end in range(len(nums)):
        # extend window
        # add nums[end] to state in O(1) in time
        if end - start + 1 == k: # moves incrementally, fixed length of 1
            # INVARIANT: size of the window is k here.
            max_ = max(max_, contents of state)
            # contract window
            # remove nums[start] from state in O(1) in time
            start += 1
    return max_
```
---
## 00. Maximum Sum of Subarrays of Size K
- https://www.hellointerview.com/learn/code/sliding-window/maximum-sum-of-subarrays-of-size-k

@[code:section::maxSum](../../../../src/leetcode/hellointerview/slidingWindow/leetcode-2461.py)

---
## 2461. Maximum Sum of Distinct Subarrays With Length K
- https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
- https://www.hellointerview.com/learn/code/sliding-window/maximum-sum-of-distinct-subarrays-with-length-k ✔️
  - add dict to track count of each num count
  - len(dict1) = k , then its distinct
  - dont forget to `increment` and `decrement` **count dict**:
    - `dict1[nums[start]] -= 1`
    - `dict1[nums[end]] = dict1.get(nums[end], 0) + 1`

@[code:section::maxSum_distinct,mySolution](../../../../src/leetcode/hellointerview/slidingWindow/leetcode-2461.py)
---
## 1423. Maximum Points You Can Obtain from Cards
> 💡inversion: outside window pattern
- https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
-  look for min sum , rather than max window sum.
- if we find anything min inside window, then outside window will become max.

@[code:13-end](../../../../src/leetcode/hellointerview/slidingWindow/leetcode-1423.py)
