class Solution:
    def numDecodings(self, s: str) -> int:
        
        n = len(s)
        dp = {n : 1}
        
        def dfs(i):
            # if i has been seen b4 
            if i in dp:
                return dp[i]
            # if no mapping
            if s[i] == "0":
                return 0
            # take one digit
            res = dfs(i + 1)
            # take 2 digits if applicable
            if i + 1 < n and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)
            # store
            dp[i] = res
            return res
        
        return dfs(0)

