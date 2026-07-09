class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        res = 0

        left = 0
        best = 0

        # go through each integer
        for right in range(len(s)):
            # add the integer to counter
            count[s[right]] = 1 + count.get(s[right], 0)
            # determine the highest frequency character
            best = max(best, count[s[right]])

            # check if window is invalid (window size - best character) = k
            while (right - left + 1) - best > k:
                # remove the left character from the window
                count[s[left]] -=1
                # move left pointer forward
                left +=1
            res = max(res, right - left + 1)


        return res