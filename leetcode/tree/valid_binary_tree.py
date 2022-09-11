"""Validate Binary Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:

```
Input: root = [2,1,3]
Output: true
```

Example 2:

```
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
```

Source: [leetcode](https://leetcode.com/problems/validate-binary-search-tree/)
"""
from .common import TreeNode


class Solution:
    def is_valid_bst(
        self, 
        root: TreeNode | None, 
        low: float = float("-inf"), 
        high: float = float("inf"),
    ) -> bool:
        """Validate Binary Search Tree
        
        Approach:
            - Traverse the tree. Must be a depth first search
            - Shortcut: if any of the subtrees are invalid. Return False.
            - If the node value is None, return True
            - Check the subtree values
                - If `not left < value < right`, return False.
            - Check the subtree validity
                - If left or right are invalid, return False
                - The left tree should be less than the min of this node and the high value
                - The right tree should be greater than the max of this node and the low
                
        Invalid Test Case:
        
                 5
               /   \
              1     6
             / \   / \
            0   9 4   7
        
        """
        if root is None:
            return True

        if not low < root.val < high:
            return False

        return self.is_valid_bst(root.left, low=low, high=root.val) and self.is_valid_bst(root.right, low=root.val, high=high)
