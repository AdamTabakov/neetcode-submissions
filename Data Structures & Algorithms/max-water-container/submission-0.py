class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1

        mx = 0

        while right > left:

            area = (right - left) * min(heights[left], heights[right])

            mx = max(mx, area)

            if heights[right] > heights[left]:
                left +=1
            else:
                right -=1
        
        return mx

            
        