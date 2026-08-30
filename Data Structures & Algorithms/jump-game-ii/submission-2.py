class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # variables
        farthest = 0
        jumps = 0
        current_end = 0
        
        # for each number in nums
        for i in range(len(nums)-1):
            # if its further than the furthest, it becomes the furthest
            farthest = max(farthest, nums[i] + i)

            # if it is at the current_end
            if i == current_end:
                # increment jump by 1, and set the current_end to the furthest
                jumps +=1
                current_end = farthest
        
        return jumps

            
