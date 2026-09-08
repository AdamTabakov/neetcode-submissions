class Solution:
    def climbStairs(self, n: int) -> int:
        # cache
        cache = [-1] * n

        # dfs
        def dfs(i):
            # if larger than n, return if i == n, so checks if its a valid path
            if i >= n:
                return i == n
            # if this has been seen in the cache already
            if cache[i] != -1:
                return cache[i]
            # add it to cache and return it
            cache[i] = dfs(i + 1) + dfs(i + 2)
            return cache[i]
        return dfs(0)

