# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def dfs_iter(root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        left, right = node.left, node.right
        node.left = right
        node.right = left

        stack.append(node.left)
        stack.append(node.right)
    return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return dfs_iter(root)