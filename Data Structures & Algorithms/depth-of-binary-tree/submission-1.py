# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs_count(root):
    if root is None:
        return 0
    stack = [(root, 1)]
    best = 0
    while stack:
        node, d = stack.pop()
        best = max(best, d)
        if node.left:
            stack.append((node.left, d+1))
        if node.right:
            stack.append((node.right, d+1))
    return best

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return dfs_count(root)