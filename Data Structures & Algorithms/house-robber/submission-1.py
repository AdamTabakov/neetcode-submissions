class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def dfs(i):
            # if it goes past the final house
            if i >= len(nums):
                return 0
            # if its already in cache
            if dp[i] != -1:
                return dp[i]
            # continue
            dp[i] = max(dfs(i + 1), nums[i] + dfs(i + 2))
            return dp[i]
            
        return dfs(0)
