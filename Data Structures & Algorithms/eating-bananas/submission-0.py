class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        arr = sorted(piles)

        left = 1
        right = max(piles)
        res = right

        while left <= right:

            mid = (left + right) // 2

            time = 0

            for p in piles:
                time += math.ceil(float(p) / mid)
            
            if time <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res