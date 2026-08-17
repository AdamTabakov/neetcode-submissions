# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            
            # if node does not exist
            if not node:
                return 0
            
            # explore left and right nodes
            left, right = dfs(node.left), dfs(node.right)

            # if the absolute difference between the 2 node depths is above 1 it's false so return -inf
            if abs(left - right) > 1:
                return float('-inf')
            
            # when the first node reaches none, get the max between the depths of left and right (0, 0) + 1, which results in the building up of depths
            return max(left, right) + 1
        
        return dfs(root) >= 0
            

            
