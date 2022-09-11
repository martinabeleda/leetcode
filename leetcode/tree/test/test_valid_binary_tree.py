import pytest

from leetcode.tree.valid_binary_tree import Solution, TreeNode

TEST_CASES = [
    [
        TreeNode(
            2,
            left=TreeNode(1),
            right=TreeNode(3),
        ),
        True,
    ],
    [
        TreeNode(
            5,
            left=TreeNode(1),
            right=TreeNode(
                4,
                left=TreeNode(3),
                right=TreeNode(6),
            ),
        ),
        False,
    ],
    [TreeNode(1), True],
    [None, True],
]


@pytest.mark.parametrize("root,expected", TEST_CASES)
def test_valid_binary_tree(root: TreeNode, expected: bool):
    assert Solution().is_valid_bst(root) == expected
