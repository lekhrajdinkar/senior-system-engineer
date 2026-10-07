# Overview
## Reference
- https://www.hellointerview.com/learn/code/dynamic-programming/fundamentals

## Overview
2 dynamic programming concepts (in Climbing Stairs problem)
  - **overlapping subproblems**: eg: `climbStairs(3)` is called twice, n=5 
  - **optimal substructure.** If we know `climbStairs(3)` and `climbStairs(4)`, then we also know `climbStairs(5)`. 

**Better solution**
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

[04_climbStarirs.excalidraw](../../draw/03/10_graph_more/04_climbStarirs.excalidraw)
