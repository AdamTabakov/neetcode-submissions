class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(start, current, total):

            if total > target:
                return
            
            if total == target:
                res.append(current[:])
                return


            for i in range(start, len(nums)):
                
                current.append(nums[i])
                backtrack(i, current, total + nums[i])
                current.pop()
        
        backtrack(0, [], 0)
        
        return res
