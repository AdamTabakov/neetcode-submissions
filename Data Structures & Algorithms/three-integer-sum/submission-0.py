class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        seen = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[left] + nums[right] + nums[i]

                if total == 0:
                    current = str(nums[i]) + str(nums[left]) + str(nums[right])

                    if current not in seen:
                        res.append([nums[left], nums[i], nums[right]])
                        seen.add(current)
                    left +=1
                    right -=1
                
                if total > 0:
                    right -=1
                
                if total < 0:
                    left +=1
        
        return res

        