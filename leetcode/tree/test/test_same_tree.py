from leetcode.tree.same_tree import Solution, TreeNode
import pytest

TEST_CASES = [
    [
        TreeNode(
            1,
            left=TreeNode(2),
            right=TreeNode(3),
        ),
        TreeNode(
            1,
            left=TreeNode(2),
            right=TreeNode(3),
        ),
        True,
    ],
    [TreeNode(1, left=TreeNode(2)), TreeNode(1, right=TreeNode(2)), False],
    [
        TreeNode(
            1,
            left=TreeNode(2),
            right=TreeNode(1),
        ),
        TreeNode(
            1,
            left=TreeNode(1),
            right=TreeNode(2),
        ),
        False,
    ],
]


@pytest.mark.parametrize("p,q,expected", TEST_CASES)
def test_same_tree(p: TreeNode, q: TreeNode, expected: bool):
    assert Solution().same_tree(p, q) == expected
