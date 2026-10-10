from typing import List


class Solution:
    # section::prefix_sums::start
    def prefix_sums(self,arr):
        n = len(arr)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1): # starts from 1
            prefix[i] = prefix[i - 1] + arr[i - 1]

        return prefix
    # section::prefix_sums::end

    # section::Problem-2::start
    # input >>> word = "prefixsum" | queries = [[0, 2], [1, 4], [3, 5]]
    def vowelStrings(self, word: str, queries: List[List[int]]) -> List[int]:
        # prepare prefix arr
        n = len(word)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i-1]+1 if word[i-1] in ['a', 'i', 'e', 'o', 'u'] else prefix[i-1]
        print ("prefix arr created: ",prefix)

        # next count vowel for each query
        res = []
        for query in queries:
            i = query[0]
            j = query[1]
            res.append(prefix[j+1] - prefix[i])
            print(f"query: {i}-{j}| {word[i:j+1]} has {prefix[j+1] - prefix[i]} vowel")

        return res
    # section::Problem-2::end

    # section::Problem-560::start
    def subarraySum(self, nums: List[int], k: int) -> int:
        pass
    # section::Problem-560::end

# ==========================
Solution().vowelStrings("prefixsum", [[0, 2], [1, 4], [3, 5]])

"""
word[0:3] -> "pre" contains 1 vowels
word[1:5]-> "refi" contains 2 vowels
word[3:6]-> "fix" contains 1 vowels
"""