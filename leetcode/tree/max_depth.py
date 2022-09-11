"""Maximum Depth of Binary Tree

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down 
to the farthest leaf node.

Example 1:

```
Input: root = [3, 9, 20, null, null, 15, 7]
Output: 3
```

Example 2:

```
Input: root = [1,null,2]
Output: 2
```

Source: [leetcode]()

"""
from .common import TreeNode


class Solution:
    def max_depth(self, root: TreeNode | None) -> int:
        """Maximum Depth of Binary Tree
        
        Approach:
            - Recursive approach. 
            - Depth first search where each call returns the depth of the subtree.
            - So the caller adds 1 to the depth of the larger subtree: `1 + max(left, right)`
            - End condition is at a leaf node (where the node is None). In this case, return 0
        
        Worked Example:
        
        For the tree: 
        
        ```
                3
               / \
              9  20
                 / \
                15  7
        ```

        - Visit root node
            - Max of node 9 and node 20
            - Visit node 20
                - Max of node 15 and node 7
                - Visit node 15
                    - Is a leaf, return 0
                - Visit node 7
                    - Is a leaf, return 0
        """
        def dfs(node: TreeNode | None) -> int:
            if node is None:
                result = 0
            else:
                result = 1 + max(dfs(node.left), dfs(node.right))
            return result
        
        return dfs(root)
            
