"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        # create defaultdic
        seen = defaultdict()

        # set the node value to the value of the Node
        seen[node] = Node(node.val)

        # create a queue
        q = deque()
        q.append(node)

        while q:
            current_node = q.popleft()
            
            for neighbour in current_node.neighbors:
                if neighbour not in seen:
                    seen[neighbour] = Node(neighbour.val)
                    q.append(neighbour)
                seen[current_node].neighbors.append(seen[neighbour])
        
        return seen[node]

        
        