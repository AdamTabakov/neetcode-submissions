# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node):
            
            # if the node does not exist, return
            if not node:
                return
            
            # if the node.val is equal to p or q, it has to be the LCA
            if q.val == node.val or p.val == node.val:
                return node

            # check the left and right side
            left = dfs(node.left)
            right = dfs(node.right)

            # if values exist on both sides, this must be the LCA
            if left and right:
                return node
            
            # otherwise, left must be the lca
            if left:
                return left
            
            # otherwise, right must be the lca
            if right:
                return right
            
            return None
        
        return dfs(root)