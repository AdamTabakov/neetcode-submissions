class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        resIdx = resLen = 0
        # start from right and move left
        for i in range(n - 1, -1, -1):
            # move from i to the end
            for j in range(i, n):
                # if the first letters are the same and there is more than 2 spaces or the middle part is already a palindrome 
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1
        return s[resIdx:resIdx + resLen]