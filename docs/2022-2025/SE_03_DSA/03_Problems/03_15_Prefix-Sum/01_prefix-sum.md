# Prefix  sum
## Reference
- https://www.hellointerview.com/learn/code/prefix-sum/overview

---
## overview
Technique for efficiently calculating the **sum of subarrays in an integer array**
- create **prefix sum array** first, takes `O(n)`
- then simply take difference, takes `O(1)` 
  - `prefix[j + 1] - prefix[i] `

---
## visual
[02-prefix-sum.excalidraw](../../draw/03/rest/02-prefix-sum.excalidraw)

---
## Problem-1: create - prefix_sums ✔️
@[code:section::prefix_sums](../../../../../src/leetcode/hellointerview/prefix-sum/Exercise-1.py)

---
## Problem-2: Count Vowels in Substrings ✔️
- https://www.hellointerview.com/learn/code/prefix-sum/count-vowels

@[code:section::Problem-2](../../../../../src/leetcode/hellointerview/prefix-sum/Exercise-1.py)

---
## 560. Subarray Sum Equals K 🟡
- https://www.hellointerview.com/learn/code/prefix-sum/subarray-sum-equals-k
- https://leetcode.com/problems/subarray-sum-equals-k/

@[code:section::Problem-560](../../../../../src/leetcode/hellointerview/prefix-sum/Exercise-1.py)