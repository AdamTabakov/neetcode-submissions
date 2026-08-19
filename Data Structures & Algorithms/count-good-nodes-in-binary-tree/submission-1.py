# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0

        def dfs(node, biggest):
            # let dfs access the good outside instead of creating it's own
            nonlocal good

            # if node does not exist
            if not node: 
                return

            # if current node value is larger than biggest, make it the new biggest 
            if node.val >= biggest:
                biggest = node.val
                good +=1
            
            left = dfs(node.left, biggest)
            right = dfs(node.right, biggest)

        dfs(root, root.val)
        return good