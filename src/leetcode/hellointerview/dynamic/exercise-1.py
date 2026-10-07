
class Solution:
    # section:problem-70-bf:start
    # recursion 👈
    # O(2 ^ n) 🔺
    def climbStairs(self, n: int) -> int:
        # dfs : base cases
        if n <= 1: return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    # section:problem-70-bf:end

    # section:problem-70-top-down:start
    # top down : recursion with "Memoization"
    # 💡Memoization :
    # - we can simply look up the result in the cache instead of recalculating it,
    # - reduces time complexity from O(2n) to O(n) | future recursive calls to the same subproblem are looked up in O(1) time
    def climbStairs2(self, n: int) -> int:
        memo = {}
        def climb_helper(i: int) -> int:
            if i <= 1:
                return 1

            # check if value is already in cache
            # before making recursive calls
            # corresponds to the green nodes in the diagram
            if i in memo:
                return memo[i]

            # store result in cache before returning
            memo[i] = climb_helper(i - 1) + climb_helper(i - 2)
            return memo[i]

        return climb_helper(n)
    # section:problem-70-top-down:end

    # section:problem-70-bottom-up:start
    # O(n)
    def stairs(self, n):
        if n <= 1:
            return 1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    # section:problem-70-bottom-up:end