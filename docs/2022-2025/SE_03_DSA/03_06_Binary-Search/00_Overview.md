# Binart search
## Reference
- https://www.hellointerview.com/learn/code/binary-search/overview

## Regular simple ✔️
- `O(log n)`

@[code:section::binarySearch,bruteForce](../../../../src/leetcode/hellointerview/binarySearch/binarySearch.py)

---
## 33. Search in Rotated Sorted Array  ✔️
- https://leetcode.com/problems/search-in-rotated-sorted-array/description/
- https://www.hellointerview.com/learn/code/binary-search/search-in-rotated-sorted-array

@[code:section::section-33](../../../../src/leetcode/hellointerview/binarySearch/binarySearch.py)

[02_bs-rotate.excalidraw](../draw/03/05/02_bs-rotate.excalidraw)

---
## 875. Koko Eating Bananas ✔️
- https://leetcode.com/problems/koko-eating-bananas/description/
- https://www.hellointerview.com/learn/code/binary-search/apple-harvest

@[code:section::section-875](../../../../src/leetcode/hellointerview/binarySearch/binarySearch.py)

[01_binary-serach.excalidraw](../draw/03/05/01_binary-serach.excalidraw)

---
## 410. Split Array Largest Sum 🟡
> Binary Search on Answer + Greedy Validation
- https://leetcode.com/problems/split-array-largest-sum/description/
- https://www.hellointerview.com/learn/code/binary-search/split-array-largest-sum

@[code:section::section-410,section-410-hi-sol](../../../../src/leetcode/hellointerview/binarySearch/binarySearch.py)

chatgpt solution
@[code:section:1-10](../../../../src/leetcode/hellointerview/binarySearch/leetcode-481.py)

---
## 1011. Minimum Shipping Capacity ✔️
> Binary Search on Answer + Greedy Validation
- https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
  - dayRequired <= days → capacity works → **try smaller capacity**
  - dayRequired > days → capacity too small → **increase capacity**
  - Time: `O(n × log(sum(weights)))`
  - Space: `O(1)`
- Another variant : https://www.hellointerview.com/learn/code/binary-search/minimum-shipping-capacity

[1011.bs-ship-capacity.excalidraw](../draw/03/05/1011.bs-ship-capacity.excalidraw)

@[code:section::section-1011](../../../../src/leetcode/hellointerview/binarySearch/binarySearch.py)

---
## 378. Kth Smallest Element in a Sorted Matrix 🟡
> can solve with heap ?
- https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
- https://www.hellointerview.com/learn/code/binary-search/kth-smallest-element-in-a-sorted-matrix

@[code:section::section-378,section-378-example](../../../../src/leetcode/hellointerview/binarySearch/binarySearch.py)
