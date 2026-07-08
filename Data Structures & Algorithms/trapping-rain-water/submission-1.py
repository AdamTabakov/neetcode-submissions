class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        # build arrays with left and right max
        leftMax = [0] * n
        rightMax = [0] * n
        
        # set boundary
        leftMax[0] = height[0]

        # find the leftmax for every slot
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        # find the rightmax for every slot
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        
        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res