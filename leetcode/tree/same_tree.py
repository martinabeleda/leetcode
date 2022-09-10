from __future__ import annotations

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def same_tree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        """Same Tree
             
        Approach:
            - Traverse the tree. Compare the visitation order. Should be the same.
            - Breadth first search:
                - put root in queue
                - pop
                    - visit: handle None condition
                    - put left in
                    - put right in
            ...
        """
        def bfs(root: TreeNode) -> list[int | None]:
            q = deque()
            result = []
            q.appendleft(root)
            
            while q:
                node = q.pop()    
                if node is None:
                    result.append(None)
                    continue
                else:
                    result.append(node.val)
                q.appendleft(node.left)
                q.appendleft(node.right)
            
            return result
            
        return bfs(p) == bfs(q)
            
        
        