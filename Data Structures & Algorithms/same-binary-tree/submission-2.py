# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2):
            
            # if node1 exists and node2 does not
            if node1 and not node2:
                return False
            # if node2 exists and node1 does not
            if node2 and not node1:
                return False

            # if both nodes exist
            if node1 and node2:
                # if the values of the nodes are not equal
                if node1.val != node2.val:
                    return False
            
                # if anything false is detected, keep the false
                if not dfs(node1.left, node2.left):
                    return False
                
                if not dfs(node1.right, node2.right):
                    return False
                

            return True
        
        return dfs(p, q)