# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root, maxSoFar):
    if root is None:
        return 0

    stack = [(root, maxSoFar)]
    count = 0
    while stack:
        node, maxSoFar = stack.pop()
        maxSoFar = max(maxSoFar, node.val)
        if node.val >= maxSoFar:
            count += 1
        
        # Push right child first so left child is processed first
        if node.right:
            stack.append((node.right, maxSoFar))
        if node.left:
            stack.append((node.left, maxSoFar))
    return count



class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return dfs(root, float('-inf'))
        
