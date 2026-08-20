class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)

        num = 0

        for _ in range(k):
            num = -heapq.heappop(heap)
        
        return num