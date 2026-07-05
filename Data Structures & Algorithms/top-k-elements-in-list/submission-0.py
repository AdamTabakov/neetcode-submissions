class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        elements = defaultdict(int)
        
        for num in nums:

            elements[num] +=1
        
        elements = sorted(elements, key = elements.get, reverse = True)

        return elements[:k]