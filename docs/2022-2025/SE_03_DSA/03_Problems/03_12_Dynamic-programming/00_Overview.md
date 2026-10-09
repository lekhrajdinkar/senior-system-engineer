# Dynamic programming ... in progress
## Reference
- https://www.hellointerview.com/learn/code/dynamic-programming/fundamentals
- https://www.hellointerview.com/learn/code/dynamic-programming/solving-a-question-with-dp

## Overview
> General Tips for Identifying Optimal Substructure
> - Assume you already know the answer for a smaller version of the input. 
> - Then see if you can use that information to solve the problem for a larger input.

problem 70 - Climbing Stairs
- understand call tree
- solve with brute force first

[04_climbStarirs.excalidraw](../../draw/03/10_graph_more/04_climbStarirs.excalidraw)

2 dynamic programming concepts
- **optimal substructure.** 
  - If we know `climbStairs(3)` and `climbStairs(4)`, then we also know `climbStairs(5)`. 
  - meaning it can be solved using recursion
- **overlapping subproblems**:
    - meaning the same recursive call is made multiple times
    - eg: `climbStairs(3)` is called twice, when n=5
  
**Better solution over brute force**
- **top-down approach** : recursive approach with **memoization**
  - store the results of subproblems
- **Bottom-Up Approach**
  - iterates from the base cases to the original problem.
  - bottom-up approach is generally more efficient because it avoids the overhead of recursive calls and function calls.

    ```
    base cases
        climbStairs(0) = 1
        climbStairs(1) = 1
    
    climbStairs(2) = climbStairs(1) + climbStairs(0) # 1 + 1 = 2
    climbStairs(3) = climbStairs(2) + climbStairs(1) # 2 + 1 = 3
    ...
    ...
    climbStairs(n) = climbStairs(n-1) + climbStairs(n-2) 
    
    ```

---
## 70. Climbing Stairs
- check **call tree** ⭐
- https://leetcode.com/problems/climbing-stairs/description/
- https://www.hellointerview.com/learn/code/dynamic-programming/fundamentals

@[code:section::problem-70-bf,problem-70-top-down,problem-70-bottom-up](../../../../../src/leetcode/hellointerview/dynamic/exercise-1.py)

---
## 198. House Robber
- in progress
- https://leetcode.com/problems/house-robber/description/
- https://www.hellointerview.com/learn/code/dynamic-programming/solving-a-question-with-dp

@[code:section::problem-198](../../../../../src/leetcode/hellointerview/dynamic/exercise-1.py)

