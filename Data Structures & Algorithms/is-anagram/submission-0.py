class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        list1 = list(s)
        list2 = list(t)
        list1 = sorted(list1)
        list2 = sorted(list2)

        return list1 == list2