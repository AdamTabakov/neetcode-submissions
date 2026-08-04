class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # set up left and right pointers
        left = 0
        right = len(nums) - 1
        
        # while right is larger than left
        while left < right:

            # find midpoint
            mid = (left + right) // 2

            # if the number at the midpoint is larger then the number on the right
            if nums[mid] > nums[right]:
                left = mid + 1
            # if the number at the midpoint is smaller than the number on the right
            else:
                right = mid
        
        return nums[left]