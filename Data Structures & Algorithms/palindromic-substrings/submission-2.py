class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        # memoization
        dp = [[False] * n for _ in range(n)]
        counter = 0
        # count from the back
        for i in range(n - 1, -1 , -1):
            # go from i to n
            for j in range(i, n):
                # current string
                curr = s[i: j + 1]
                # if found before, continue
                if dp[i][j] != False:
                    continue
                else:
                    # if the ends have the same letter and the string is smaller than 2 characters, or middle is a palindrome
                    if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                        dp[i][j] = True
                        counter +=1
        
        return counter