class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        count1 = {}
        count2 = {}

        for i in range(len(s1)):
            count1[s1[i]] = 1 + count1.get(s1[i], 0)
            count2[s2[i]] = 1 + count2.get(s2[i], 0)

        if count1 == count2:
            return True
        
        left = 0

        for right in range(len(s1), len(s2)):
            # add new character
            count2[s2[right]] = 1 + count2.get(s2[right], 0)

            # remove old character
            count2[s2[left]] -= 1

            if count2[s2[left]] == 0:
                del count2[s2[left]]

            left += 1

            if count1 == count2:
                return True

        return False


        