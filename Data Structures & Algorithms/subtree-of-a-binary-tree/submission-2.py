# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # depth first search
        def dfs(node, subnode):
            
            # if node doesnt exist, go back
            if not node:
                return

            # check if the current node is identical to subnode
            confirmation = check(node, subnode)
            
            # if it is, return true
            if confirmation:
                return True
            
            # otherwise, check left 
            left = dfs(node.left, subnode)

            # if left is true, return true
            if left == True:
                return True
            
            # otherwise check right
            right = dfs(node.right, subnode)
            # if right is true, return true
            if right == True:
                return True
            
            return False
            

        # helper function to check if theyre identical
        def check(node, subnode):
            
            # if only one of the nodes exist
            if node and not subnode:
                return False
            if subnode and not node:
                return False

            # if both exist
            if node and subnode:
                # if values arent equal
                if node.val != subnode.val:
                    return False
                
                # if the left isn't the same
                if not check(node.left, subnode.left):
                    return False
                
                # if the right isnt the same
                if not check(node.right, subnode.right):
                    return False
            
            # otherwise
            return True
            
        return dfs(root, subRoot)
            


