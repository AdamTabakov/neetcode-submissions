class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for ch in nums:

            if ch in seen:
                return True
            else:
                seen.add(ch)
        return False
        