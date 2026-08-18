# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(node, subnode):
            
            if not node:
                return

            confirmation = check(node, subnode)
            
            if confirmation:
                return True
            
            left = dfs(node.left, subnode)

            if left == True:
                return True
            
            right = dfs(node.right, subnode)
            if right == True:
                return True
            
            return False
            

        

        def check(node, subnode):
            
            if node and not subnode:
                return False
            
            if subnode and not node:
                return False

            if node and subnode:
                if node.val != subnode.val:
                    return False
                
                if not check(node.left, subnode.left):
                    return False
                
                if not check(node.right, subnode.right):
                    return False
            
            return True
            
        return dfs(root, subRoot)
            


