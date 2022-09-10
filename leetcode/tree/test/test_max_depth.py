from leetcode.tree.max_depth import Solution, TreeNode
import pytest

TEST_CASES = [
    [
        TreeNode(
            3, 
            left=TreeNode(9), 
            right=TreeNode(
                20, 
                left=TreeNode(15), 
                right=TreeNode(7),
            ),
        ), 
        3
    ],
    [TreeNode(1, right=TreeNode(2)), 2],
]


@pytest.mark.parametrize("tree,expected", TEST_CASES)
def test_max_depth(tree: TreeNode, expected: int):
    assert Solution().max_depth(tree) == expected
