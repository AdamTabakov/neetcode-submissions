class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        window_start = 0
        score = 0

        best = 1
        curr = set()
        curr.add(s[0])

        

        for i in range(1, len(s)):

            if s[i] in curr:
                
                while s[i] in curr:
                    curr.remove(s[window_start])
                    window_start +=1

                    
                
                
                
            curr.add(s[i])
            best = max((i - window_start + 1), best)

        return best
            






        