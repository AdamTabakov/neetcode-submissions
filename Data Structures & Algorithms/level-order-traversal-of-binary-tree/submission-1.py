# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = []
        q = deque()
        
        # if there is a root, add it to q
        if root:
            q.append(root)
        
        # while the q exists
        while q:
            temp_vals = []
            # go through each item in q and add its children
            for i in range(len(q)):
                node = q.popleft()

                temp_vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            values.append(temp_vals)
        
        return values

            
