from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        """In Order traversal

        Traverse a binary tree in order:
            - Depth first search
            - Define a result array
            - Recursively visit the left subtree
            - Visit root
            - Recursively visit right
        """
        if not root:
            return []

        result = []
        self.dfs(root, result)
        return result

    def dfs(self, node: Optional[TreeNode], result: List[int]):
        if not node:
            return

        self.dfs(node.left, result)
        result.append(node.val)
        self.dfs(node.right, result)
