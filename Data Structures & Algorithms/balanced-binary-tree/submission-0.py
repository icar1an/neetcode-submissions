# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def binaryBalance(node):
    if node is None:
        return True
    if abs(maxDepth(node.left) - maxDepth(node.right)) > 1:
        return False
    else:
        return binaryBalance(node.left) and binaryBalance(node.right)
    
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return binaryBalance(root)