class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        maximum = max(piles)

        left, right = 1, maximum
        best = maximum

        while left <= right:
            mid = (left + right) // 2

            if self.check(mid, piles, h):
                best = mid
                right = mid - 1
            else:
                left = mid + 1

        return best

            
    def check(self, mid, piles, h):
        hours = 0

        for pile in piles:
            hours = hours + math.ceil(pile / mid)
        
        if hours > h:
            return False
        else:
            return True

        
