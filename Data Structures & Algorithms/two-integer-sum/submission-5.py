class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indexed_nums = []
        for i in range(len(nums)):
            indexed_nums.append([nums[i], i])
        indexed_nums.sort()

        left = 0
        right = len(nums) - 1

        while right > left:

            total = indexed_nums[right][0] + indexed_nums[left][0]

            if total == target:
                idx1 = indexed_nums[left][1]
                idx2 = indexed_nums[right][1]
                return [min(idx1, idx2), max(idx1, idx2)]
                        
            else:
                if target > total:
                    left +=1 
                elif target < total:
                    right -=1