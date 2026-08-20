class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create max-heap
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) != 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            
            new = x - y
            heapq.heappush(heap, -new)

        return -heapq.heappop(heap)