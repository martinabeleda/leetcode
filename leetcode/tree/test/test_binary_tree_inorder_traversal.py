from leetcode.tree.binary_tree_inorder_traversal import Solution, TreeNode


def test_inorder_traversal():
    root = TreeNode(
        1,
        right=TreeNode(
            2,
            left=TreeNode(3),
        ),
    )
    expected = [1, 3, 2]
    assert Solution().inorder_traversal(root) == expected


def test_inorder_traversal_empty():
    root = None
    expected = []
    assert Solution().inorder_traversal(root) == expected


def test_inorder_traversal_root():
    root = TreeNode(1)
    expected = [1]
    assert Solution().inorder_traversal(root) == expected
